import operator

from dominate.tags import li, ul

from iolanta.facet import Facet
from iolanta.namespaces import IOLANTA
from mkdocs_iolanta.iolanta import render
from octadocs_ibis.models import IBIS


class PositionsForIssue(Facet):
    """List positions to answer the Issue."""

    sparql_query = '''
    SELECT * WHERE {
        ?position ibis:responds-to $issue .
    } ORDER BY ?position
    '''

    def render(self):
        rows = self.query(self.sparql_query, issue=self.uriref)
        positions = list(map(operator.itemgetter('position'), rows))

        return ul(
            li(
                render(
                    position,
                    environments=[IOLANTA.html],
                    iolanta=self.iolanta,
                ),
            ) for position in positions
        )
