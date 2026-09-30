from __future__ import annotations
import ast
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError

class MigratePythonTool(ToolContract):
    metadata = ToolMetadata(
        name="migrate-python",
        description="Apply deterministic, syntax-aware Python migration rules without executing source code.",
        input_schema={"type":"object","required":["source","rules"],"properties":{"source":{"type":"string"},"rules":{"type":"array","items":{"type":"string"}}},"additionalProperties":False},
        limitations=("Rules are intentionally explicit and limited to safe source transformations.", "Unrecognized rules are reported rather than guessed."),
    )
    def validate(self, inputs):
        super().validate(inputs)
        if not isinstance(inputs["source"], str) or not inputs["source"].strip(): raise ToolValidationError("source must be non-empty")
        if not isinstance(inputs["rules"], list) or not all(isinstance(x,str) for x in inputs["rules"]): raise ToolValidationError("rules must be a list of strings")
    def execute(self, inputs):
        source=inputs["source"]; rules=inputs["rules"]; tree=ast.parse(source)
        changed=[]; unsupported=[]
        for rule in rules:
            if rule == "rename-print-function":
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print": node.func.id="log"
                changed.append(rule)
            elif rule == "replace-xrange-with-range":
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "xrange": node.func.id="range"
                changed.append(rule)
            else: unsupported.append(rule)
        migrated=ast.unparse(tree)
        return ToolResult(True,{"migrated_source":migrated,"applied_rules":changed,"unsupported_rules":unsupported})
