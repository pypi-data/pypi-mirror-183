from iolanta.facet import Facet
from iolanta.renderer import render
from mkdocs_iolanta_tables.models import TABLE


class Th(Facet):
    """Render a table column header."""

    def html(self):
        """Render the column."""
        return render(
            node=self.iri,
            iolanta=self.iolanta,
            environments=[TABLE.th],
        )
