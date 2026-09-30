from __future__ import annotations
import ast
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError

class ValidateMigrationTool(ToolContract):
    metadata=ToolMetadata(
        name="validate-migration", description="Validate migrated Python source for syntax and simple migration safety conditions.",
        input_schema={"type":"object","required":["source"],"properties":{"source":{"type":"string"}},"additionalProperties":False},
        limitations=("Validation is static and Python-focused.", "Behavioral equivalence requires project-specific tests."),)
    def validate(self, inputs):
        super().validate(inputs)
        if not isinstance(inputs["source"],str) or not inputs["source"].strip(): raise ToolValidationError("source must be non-empty")
    def execute(self, inputs):
        source=inputs["source"]
        issues=[]
        try: tree=ast.parse(source)
        except SyntaxError as exc: return ToolResult(True,{"valid":False,"issues":[{"type":"syntax","message":str(exc)}]})
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"eval","exec"}:
                issues.append({"type":"unsafe_dynamic_execution","name":node.func.id,"line":node.lineno})
        return ToolResult(True,{"valid":not issues,"issues":issues})
