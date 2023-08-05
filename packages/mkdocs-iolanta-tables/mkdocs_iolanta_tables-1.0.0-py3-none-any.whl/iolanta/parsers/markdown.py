import json
import re
from io import StringIO
from typing import Iterable, Optional, TextIO

import frontmatter
from rdflib import RDF, URIRef
from yaml.scanner import ScannerError

from iolanta.loaders import Loader
from iolanta.models import LDContext, LDDocument, Quad
from iolanta.parsers.errors import YAMLError
from iolanta.parsers.json import JSON, assign_key_if_not_present
from iolanta.parsers.yaml import YAML
from mkdocs_iolanta.types import MKDOCS

try:  # noqa
    from yaml import CSafeLoader as SafeLoader  # noqa
except ImportError:
    from yaml import SafeLoader  # type: ignore   # noqa


class Markdown(YAML):
    """Load YAML data."""

    def as_jsonld_document(self, raw_data: TextIO) -> LDDocument:
        """Read YAML content and adapt it to JSON-LD format."""
        raw_data.seek(0)
        return frontmatter.load(raw_data).metadata

    def construct_page_url(self, iri: URIRef) -> str:
        """Construct URL of a page."""
        match = re.match('^docs://(?P<path>.+)$', str(iri))
        if match is None:
            raise ValueError(f'Could not decode URL: {iri}')

        url = match.groupdict()['path']

        url = re.sub(
            r'(index)?\.md$',
            '',
            url,
        )

        if not url.endswith('/'):
            url = f'{url}/'

        if url == '/':
            url = ''

        return f'/{url}'

    def as_quad_stream(
        self,
        raw_data: TextIO,
        iri: Optional[URIRef],
        context: LDContext,
        root_loader: Loader,
    ) -> Iterable[Quad]:
        """Assign mkdocs:url and generate quad stream."""
        try:
            json_data = self.as_jsonld_document(raw_data)
        except ScannerError as err:
            raise YAMLError(
                iri=iri,
                error=err,
            ) from err

        json_data = assign_key_if_not_present(
            document=json_data,
            key='mkdocs:url',
            default_value=self.construct_page_url(iri),
        )

        quad_stream = JSON().as_quad_stream(
            raw_data=StringIO(json.dumps(json_data, ensure_ascii=False)),
            iri=iri,
            context=context,
            root_loader=root_loader,
        )

        return [
            Quad(iri, RDF.type, MKDOCS.Page, iri),
            *quad_stream,
        ]
