import dataclasses
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path
from typing import Iterable, List, Optional, TextIO, Type, Union

from rdflib import URIRef
from urlpath import URL

from iolanta.context import merge
from iolanta.conversions import path_to_url, url_to_path
from iolanta.ensure_is_context import NotAContext, ensure_is_context
from iolanta.loaders.base import Loader
from iolanta.loaders.local_file import LocalFile
from iolanta.models import LDContext, LDDocument, Quad
from iolanta.parsers.base import Parser
from mkdocs_iolanta.types import MKDOCS


def merge_contexts(*contexts: LDContext) -> LDContext:
    return reduce(
        merge,
        filter(bool, contexts),
        {},
    )


@dataclass(frozen=True)
class LocalDirectory(Loader):
    """
    Retrieve Linked Data from a file on local disk.

    Requires URL with file:// scheme as input.
    """

    root_directory: Optional[Path] = None
    context_filenames: List[str] = field(
        default_factory=lambda: [
            'context.yaml',
            'context.json',
        ],
    )
    default_context: Optional[LDContext] = field(default=None, repr=False)

    def directory_level_context(self, path: Path) -> Optional[LDContext]:
        for file_name in self.context_filenames:
            if (context_path := path / file_name).is_file():
                document = LocalFile().as_jsonld_document(
                    url=path_to_url(context_path),
                )

                if document:
                    try:
                        return ensure_is_context(document)
                    except NotAContext as err:
                        raise dataclasses.replace(
                            err,
                            path=context_path,
                        )

    def choose_parser_class(self, url: URL) -> Type[Parser]:
        """Choose parser class based on file extension."""
        raise ValueError('This is a directory')

    def as_quad_stream(
        self,
        url: Union[URL, Path],
        iri: Optional[URIRef],
        root_loader: Loader,
    ) -> Iterable[Quad]:
        """Extract a sequence of quads from a local file."""
        path = url_to_path(url) if isinstance(url, URL) else url

        if not path.is_dir():
            yield from LocalFile(
                context=self.default_context,
            ).as_quad_stream(
                url=url,
                root_loader=root_loader,
                iri=iri,
            )
            return

        context = merge_contexts(
            self.default_context,
            self.directory_level_context(path),
        )

        for child in path.iterdir():
            child_iri = URIRef(f'{iri}{child.name}')

            if child.is_dir():
                child_iri += '/'

                yield from LocalDirectory(
                    default_context=context,
                ).as_quad_stream(
                    url=child,
                    iri=child_iri,
                    root_loader=root_loader,
                )

            elif child.stem != 'context':
                yield from LocalFile(
                    context=context,
                ).as_quad_stream(
                    url=path_to_url(child),
                    iri=child_iri,
                    root_loader=root_loader,
                )

            if iri is not None:
                yield Quad(
                    subject=child_iri,
                    predicate=MKDOCS.isChildOf,
                    object=iri,
                    graph=URIRef(
                        'https://iolanta.tech/loaders/local-directory',
                    ),
                )

    def as_file(self, url: URL) -> TextIO:
        """Construct a file-like object."""
        path = url_to_path(url)
        with path.open() as text_io:
            return text_io

    def as_jsonld_document(
        self,
        url: URL,
        iri: Optional[URIRef] = None,
    ) -> LDDocument:
        """As JSON-LD document."""
        raise ValueError('This is a directory.')

    def find_context(self, url: URL) -> LDContext:
        """Traverse the directories and construct context."""
        return merge_contexts(
            self.default_context,
            *self.contexts_by_url(url),
        )

    def contexts_by_url(self, url: URL) -> Iterable[LDContext]:
        return [
            self.as_jsonld_document(
                url=URL(f'file://{context_file}'),
            )
            for context_file in self.context_files_by_url(url)
        ]

    def context_files_by_url(self, url: URL) -> Iterable[Path]:
        """Yield all contexts by URL."""
        ancestor_directories = self.ancestors_by_url(url)
        for directory in ancestor_directories:
            for filename in self.context_filenames:
                if (context_file := directory / filename).exists():
                    yield context_file

    def ancestors_by_url(self, url: URL) -> Iterable[Path]:
        """Find all ancestor directories to this path."""
        if self.root_directory is None:
            raise ValueError('Please specify a root directory.')

        root_directory = self.root_directory.absolute()
        for ancestor in reversed(url_to_path(url).parents):
            ancestor = ancestor.absolute()

            # Replace with .is_relative_to() for Python 3.9.
            if str(ancestor).startswith(str(root_directory)):
                yield ancestor
