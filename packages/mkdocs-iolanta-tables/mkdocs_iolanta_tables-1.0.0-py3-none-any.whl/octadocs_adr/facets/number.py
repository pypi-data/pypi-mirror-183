import functools
import operator
from pathlib import Path

import funcy
from dominate.tags import a, code, div, h1, h2, p

from iolanta.facet import Facet
from mkdocs_iolanta.iolanta import render
from octadocs_adr.models import ADR


class Number(Facet):
    """ADR List item."""

    def render(self):
        row = self.query(
            (Path(__file__).parent / 'sparql/number.sparql').read_text(),
            adr_page=self.iri,
        ).first

        return 'ADR{:03d}'.format(row['number'].value)
