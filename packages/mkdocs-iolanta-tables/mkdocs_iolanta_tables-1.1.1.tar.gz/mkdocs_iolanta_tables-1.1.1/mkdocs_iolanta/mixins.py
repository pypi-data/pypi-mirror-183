import logging
import operator
import re
from functools import cached_property, partial
from pathlib import Path
from typing import Callable, Dict, Optional, TypedDict

import rdflib
from mkdocs.config import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation
from mkdocs.structure.pages import Page
from rdflib import SDO, ConjunctiveGraph, Namespace, URIRef
from typer import Typer

from iolanta.conversions import path_to_url
from iolanta.errors import FacetNotFound
from iolanta.iolanta import Iolanta
from iolanta.loaders.base import term_for_python_class
from iolanta.loaders.local_directory import merge_contexts
from iolanta.models import LDContext, Triple
from iolanta.namespaces import IOLANTA
from iolanta.parsers.yaml import YAML
from iolanta.renderer import Render, render
from mkdocs_iolanta.conversions import iri_by_page
from mkdocs_iolanta.storage import save_graph
from mkdocs_iolanta.types import MKDOCS

logger = logging.getLogger(__name__)


class TemplateContext(TypedDict):
    """Context for the native MkDocs page rendering engine."""

    graph: rdflib.ConjunctiveGraph
    iri: rdflib.URIRef
    this: rdflib.URIRef
    local: rdflib.Namespace
    render: Callable[[rdflib.URIRef], str]

    # FIXME this is hardcode and should be removed
    rdfs: rdflib.Namespace


class OctadocsMixin(BasePlugin):
    """MkDocs plugin that aims to extend Octadocs functionality."""

    iolanta: Iolanta
    namespaces: Optional[Dict[str, Namespace]] = None
    plugin_data_dir: Path
    docs_dir: Path

    @property
    def ldflex(self):
        return self.iolanta.ldflex

    @property
    def graph(self) -> ConjunctiveGraph:
        return self.iolanta.graph

    def typer(self) -> Optional[Typer]:
        """Return a CLI command for octadocs app."""

    @cached_property
    def templates_path(self) -> Optional[Path]:
        """Templates associated with the plugin."""
        path = Path(__file__).parent / 'templates'
        if path.exists():
            return path

    def named_contexts(self) -> Dict[str, LDContext]:
        """Named contexts."""
        return {}

    def vocabularies(self) -> Dict[URIRef, Path]:
        """Pieces of structured data to load into graph."""
        return {}

    @property
    def cache_path(self) -> Path:
        return self.docs_dir.parent / '.cache/octadocs'

    def on_config(self, config, **kwargs):
        """Adjust system configuration to suit this plugin."""
        # Make plugin's templates available to MkDocs
        if self.templates_path:
            config['theme'].dirs.append(str(self.templates_path))

        docs_dir = Path(config['docs_dir'])
        self.docs_dir = docs_dir

        config.setdefault('extra', {})

        try:
            self.iolanta = config['extra']['iolanta']
        except KeyError:
            # FIXME we're not loading the graph from cache.
            #   That's because we do not have any kind of cache invalidation.
            self.iolanta = Iolanta()

        config['extra']['iolanta'] = self.iolanta

        self.bind_namespaces()

    def inference(self):
        """
        Apply inference, if any.

        This function is for the plugins to override. They may run SPARQL
        or whatever they want to do on the graph.
        """

    @property
    def query(self):
        return self.iolanta.query

    def insert(self, *triples: Triple):
        """Insert triples into graph."""
        graph = term_for_python_class(self.__class__)
        quads = map(
            operator.methodcaller('as_quad', graph),
            triples,
        )
        self.graph.addN(quads)

    def save_graph_to_cache(self, config: Config):
        """Pickle the graph to reuse it in CLI and other tools."""
        if config['extra'].get('save_graph_to_cache'):
            return

        save_graph(
            graph=self.iolanta.graph,
            path=self.cache_path,
        )
        logger.info('Saved graph to disk for CLI to use.')

        config['extra']['save_graph_to_cache'] = True

    def bind_namespaces(self):
        namespaces = self.namespaces or {}

        # Default namespaces for Octadocs.
        namespaces.update({
            'mkdocs': MKDOCS,
            'iolanta': IOLANTA,
            'schema': SDO,

            'docs': Namespace('docs://'),
            'local': Namespace('local:'),
        })

        self.iolanta.bind_namespaces(**namespaces)

    def on_page_markdown(
        self,
        markdown: str,
        page: Page,
        config: Config,
        files: Files,
    ):
        """Inject page template path, if necessary."""
        page.iri = iri_by_page(page)

        try:
            template_url = Render(
                ldflex=self.ldflex,
            ).find_facet_iri(
                node=page.iri,
                environments=[URIRef(MKDOCS)],
            )
        except FacetNotFound:
            return markdown

        page.meta['template'] = re.sub(
            '^templates:/*',
            '',
            template_url,
        )

        return markdown

    @cached_property
    def id_by_page(self) -> Dict[URIRef, URIRef]:
        """Retrieve the best suitable IRI for an MkDocs page."""
        rows = self.query(
            'SELECT ?page ?this WHERE { ?this mkdocs:subjectOf ?page . }',
        )

        return {
            row['page']: row['this']
            for row in rows
        }

    def on_shutdown(self) -> None:
        self.save_graph_to_cache(config={'extra': {}})

    def on_build_error(self, error):
        """Save the graph to a file on build error."""
        self.save_graph_to_cache(config={'extra': {}})

    def on_post_build(self, config: Config):
        """Save the graph to a file on disk."""
        self.save_graph_to_cache(config)

    def _inference_and_navigation(
        self,
        config: Config,
        nav: Navigation,
    ) -> Navigation:
        if config['extra'].get('_inference_and_navigation'):
            return nav

        # This must run after all on_files() handlers of all plugins, but before
        # any page rendering and facets. Nav calculation depends on inference,
        # that's why we call it here in on_nav().
        self.iolanta.infer()

        config['extra']['_inference_and_navigation'] = True

        return nav

    def on_nav(
        self,
        nav: Navigation,
        config: Config,
        files: Files,
    ) -> Navigation:
        """Update the site's navigation from the knowledge graph."""
        return self._inference_and_navigation(
            config=config,
            nav=nav,
        )

    def on_page_context(
        self,
        context: TemplateContext,
        page: Page,
        config: Config,
        nav: Page,
    ) -> TemplateContext:
        """Attach the views to certain pages."""
        context['render'] = partial(
            render,
            iolanta=self.iolanta,
        )
        return context

    def _add_files(self, config: Config):
        if config['extra'].get('_add_files'):
            return

        default_context = config['extra']['default_context'] = self._construct_default_context(config)

        self.iolanta.add(
            path_to_url(
                Path(__file__).parent / 'yaml/octadocs.yaml',
            ),
            context=default_context,
        )

        self.iolanta.add(
            path_to_url(
                Path(__file__).parent / 'yaml/iolanta.yaml',
            ),
            context=default_context,
        )

        docs_dir_url = path_to_url(self.docs_dir)

        self.iolanta.add(
            docs_dir_url,
            graph_iri=URIRef('docs://'),
            context=default_context,
        )

        config['extra']['_add_files'] = True

    def on_files(self, files: Files, config: Config):
        """Extract metadata from files and compose the site graph."""
        self._add_files(config)

        self.inference()

    def _construct_default_context(self, config: Config):
        context_paths = [
            Path(__file__).parent / 'yaml/context.yaml',
            *config['extra']['contexts'],
        ]

        context_contents = [
            YAML().as_jsonld_document(path.open('r'))
            for path in context_paths
        ]

        return merge_contexts(*context_contents)
