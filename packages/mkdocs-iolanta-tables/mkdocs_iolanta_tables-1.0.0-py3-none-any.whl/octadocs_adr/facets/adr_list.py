import functools
import operator
from pathlib import Path

import funcy
from dominate.tags import div

from iolanta.facet import Facet
from mkdocs_iolanta.iolanta import render
from octadocs_adr.models import ADR


class List(Facet):
    def render(self):
        rows = self.query(
            (Path(__file__).parent / 'sparql/list.sparql').read_text(),
            index=self.iri,
        )

        page_iris = funcy.pluck('adr_page', rows)

        return div(
            *[
                render(
                    page_iri,
                    iolanta=self.iolanta,
                    environments=[ADR.list],
                )
                for page_iri in page_iris
            ]
        )
