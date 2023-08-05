import functools
import operator
from pathlib import Path

import funcy
from dominate.tags import a, code, div, h1, h2, p
from dominate.util import raw

from iolanta.facet import Facet
from mkdocs_iolanta.iolanta import render
from octadocs_adr.models import ADR

TEMPLATE = '''
!!! note "TL;DR"
    {}

<div class="admonition note">
<p class="admonition-title">TL;DR</p>
<p>boo</p>
</div>
'''


class Description(Facet):
    """ADR Description."""

    def render(self):
        row = self.query(
            (Path(__file__).parent / 'sparql/description.sparql').read_text(),
            adr_page=self.iri,
        ).first

        return div(
            p(
                'TL;DR',
                cls='admonition-title',
            ),
            p(
                raw(row['description']),
            ),
            cls='admonition note',
        ) if row else ''
