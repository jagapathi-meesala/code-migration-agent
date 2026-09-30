from __future__ import annotations
import difflib
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError

class CompareVersionsTool(ToolContract):
    metadata=ToolMetadata(
        name="compare-versions", description="Produce a unified diff and change statistics between source versions.",
        input_schema={"type":"object","required":["before","after"],"properties":{"before":{"type":"string"},"after":{"type":"string"}},"additionalProperties":False},
        limitations=("Comparison is textual and does not prove semantic equivalence.", "Binary files are unsupported."),)
    def validate(self, inputs):
        super().validate(inputs)
        if not all(isinstance(inputs[k],str) for k in ("before","after")): raise ToolValidationError("before and after must be strings")
    def execute(self, inputs):
        a=inputs["before"].splitlines(); b=inputs["after"].splitlines(); diff=list(difflib.unified_diff(a,b,fromfile="before",tofile="after",lineterm=""))
        additions=sum(1 for x in diff if x.startswith("+") and not x.startswith("+++")); deletions=sum(1 for x in diff if x.startswith("-") and not x.startswith("---"))
        return ToolResult(True,{"diff":"\n".join(diff),"additions":additions,"deletions":deletions,"changed":bool(additions or deletions)})
