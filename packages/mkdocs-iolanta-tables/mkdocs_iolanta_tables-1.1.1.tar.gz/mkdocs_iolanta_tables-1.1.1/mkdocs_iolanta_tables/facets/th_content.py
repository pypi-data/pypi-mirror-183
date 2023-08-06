from pathlib import Path
from typing import Optional, TypedDict

import funcy
from dominate.tags import a  # noqa: WPS347
from rdflib import Literal

from iolanta.facet import Facet


class ThContentRow(TypedDict):
    """A few properties of the object we use as row heading."""

    label: Optional[Literal]
    symbol: Optional[Literal]
    url: Optional[Literal]
    comment: Optional[Literal]


class ThContent(Facet):
    """Render a table column header."""

    def html(self):
        """Render the column."""
        row: ThContentRow = funcy.first(
            self.query(
                (
                    Path(__file__).parent / 'sparql/th_content.sparql'
                ).read_text(),
                iri=self.iri,
            ),
        )

        if row.get('url'):
            return self._render_link(row)

        return self._render_heading(row)

    def _render_link(self, row: ThContentRow):
        return a(
            self._render_heading(row),
            href=row['url'],
        )

    def _render_heading(self, row: ThContentRow):
        label = row.get('label') or self._render_fallback()

        if symbol := row.get('symbol'):
            label = f'{symbol} {label}'

        return label

    def _render_fallback(self):
        return str(self.iri).replace(
            'local:', '',
        ).replace(
            '_', ' ',
        ).replace(
            '-', ' ',
        ).capitalize()
