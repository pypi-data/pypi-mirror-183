from typing import Protocol

from rdflib import URIRef
from rdflib.term import Node

from iolanta.iolanta import Iolanta


class PythonFacet(Protocol):
    """Prototype of a Python facet function."""

    def __call__(
        self,
        iolanta: Iolanta,
        node: Node,
        environment: URIRef,
    ) -> str:
        ...
