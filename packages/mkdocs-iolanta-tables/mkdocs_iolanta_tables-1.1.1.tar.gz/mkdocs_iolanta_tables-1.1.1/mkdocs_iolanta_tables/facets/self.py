from dataclasses import dataclass

from documented import DocumentedError
from more_itertools import first
from rdflib import URIRef

from iolanta.facet import Facet
from iolanta.renderer import render
from mkdocs_iolanta_tables.models import TABLE


@dataclass
class MissingTableInstanceClass(DocumentedError):
    """
    Table does not have an instance class defined.

    Table IRI: `{self.table_iri}`

    For this table, you had tried to render `table:self` column. This cannot be
    executed at this time because the table does not have an associated
    `table:class`. Please create one:

    ```yaml
    "@context":
      $import: table
    $id: {self.table_iri}
    class: <class of things you wish to display in your table>
    ```
    """

    table_iri: URIRef


class SelfFacet(Facet):
    """Render table:self property."""

    def html(self):
        """Call rendering for the underlying class of the table."""
        if self.environment is None:
            raise ValueError(
                f'Facet {self} was called with no environment specified.',
            )

        rows = self.query(
            query_text='''
            SELECT * WHERE {
                $table table:class ?cls .
            }
            ''',
            table=self.environment,
        )

        try:
            instance_class = first(rows)['cls']
        except ValueError as err:
            raise MissingTableInstanceClass(
                table_iri=self.environment,
            ) from err

        return render(
            node=instance_class,
            iolanta=self.iolanta,
            environments=[TABLE.th],
        )
