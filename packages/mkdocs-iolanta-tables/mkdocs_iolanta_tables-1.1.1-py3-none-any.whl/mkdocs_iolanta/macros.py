from functools import partial
from typing import Any, Dict, List, Optional

import rdflib
from mkdocs_macros.plugin import MacrosPlugin
from rdflib import URIRef
from rdflib.plugins.sparql.processor import SPARQLResult

from iolanta.iolanta import Iolanta
from iolanta.renderer import render
from mkdocs_iolanta.types import LOCAL


def sparql(
    instance: rdflib.ConjunctiveGraph,
    query: str,
    **kwargs: str,
) -> SPARQLResult:
    bindings = {
        argument_name: argument_value
        for argument_name, argument_value in kwargs.items()
    }

    return instance.query(query, initBindings=bindings)


def _render_as_row(row: Dict[rdflib.Variable, Any]) -> str:  # type: ignore
    """Render row of a Markdown table."""
    formatted_row = ' | '.join(row.values())
    return f'| {formatted_row} |'


def table(query_result: SPARQLResult) -> str:
    """Render as a Markdown table."""
    headers = ' | '.join(str(cell) for cell in query_result.vars)

    rows = '\n'.join(
        _render_as_row(row)
        for row in query_result.bindings
    )

    separators = '| ' + (' --- |' * len(query_result.vars))  # noqa: WPS336

    return f'''
---
| {headers} |
{separators}
{rows}
'''


def url(
    resource: rdflib.URIRef,
    graph: rdflib.ConjunctiveGraph,
) -> Optional[str]:
    """Convert a URIRef to a clickable URL."""
    bindings = graph.query(
        'SELECT ?url WHERE { ?resource mkdocs:subjectOf/mkdocs:url ?url . } ',
        initBindings={
            'resource': resource,
        },
    ).bindings

    if not bindings:
        return None

    return '/' + bindings[0][rdflib.Variable('url')].value


def label(
    resource: rdflib.URIRef,
    graph: rdflib.ConjunctiveGraph,
) -> Optional[str]:
    """Convert a URIRef to a clickable URL."""
    bindings = graph.query(
        'SELECT ?label WHERE { ?resource rdfs:label ?label . } ',
        initBindings={
            'resource': resource,
        },
    ).bindings

    if not bindings:
        return None

    return bindings[0][rdflib.Variable('label')].value


def macro_render(
    thing: str,
    environments: Optional[List[str]] = None,
    iolanta: Iolanta = None,
):
    if ':' not in thing:
        thing = f'local:{thing}'

    if isinstance(environments, str):
        environments = [environments]

    elif environments is None:
        environments = []

    environments = [
        URIRef(f'local:{environment}') if (
            isinstance(environment, str)
            and ':' not in environment
        ) else environment
        for environment in environments
    ]

    return render(
        node=URIRef(thing),
        iolanta=iolanta,
        environments=[URIRef(environment) for environment in environments],
    )


def define_env(env: MacrosPlugin) -> MacrosPlugin:  # noqa: WPS213
    """Create mkdocs-macros Jinja environment."""
    env.filter(sparql)
    env.filter(table)

    # octiron = env.variables.octiron
    # env.variables.update(octiron.namespaces)
    env.variables['LOCAL'] = LOCAL
    env.variables['local'] = LOCAL

    iolanta = env.variables.iolanta

    env.macro(
        partial(
            macro_render,
            iolanta=iolanta,
        ),
        name='render',
    )

    env.variables['URIRef'] = rdflib.URIRef

    return env
