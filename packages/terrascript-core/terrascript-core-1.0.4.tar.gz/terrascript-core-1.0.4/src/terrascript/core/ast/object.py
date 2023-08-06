from typing import List, Optional

import attr

from .base import Element, __compiler__, render

__t__ = __compiler__.compile(
    """{{{key}}}{{#if label}} "{{{label}}}"{{/if}} {{{op}}} {
{{#each elements}}
    {{{render this}}}
{{/each}}
}"""
)


@attr.define
class AstObject(Element):
    key: str
    op: str = ""
    label: Optional[str] = None
    elements: List[Element] = attr.field(factory=list)

    def render(self) -> str:
        return __t__(self, helpers={"render": render})
