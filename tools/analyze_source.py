from __future__ import annotations
import ast
from contracts.tool_contract import ToolContract, ToolMetadata, ToolResult, ToolValidationError

class AnalyzeSourceTool(ToolContract):
    metadata = ToolMetadata(
        name="analyze-source",
        description="Analyze Python source for imports, syntax validity, functions, classes, and migration-relevant constructs.",
        input_schema={"type":"object","required":["source"],"properties":{"source":{"type":"string"}},"additionalProperties":False},
        limitations=("Currently parses Python source only.", "Static analysis does not execute imported code."),
    )
    def validate(self, inputs):
        super().validate(inputs)
        if not isinstance(inputs["source"], str) or not inputs["source"].strip():
            raise ToolValidationError("source must be a non-empty string")
    def execute(self, inputs):
        source = inputs["source"]
        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            return ToolResult(False, error={"type":"syntax_error","message":str(exc),"line":exc.lineno,"column":exc.offset})
        imports=[]; functions=[]; classes=[]; calls=[]
        for node in ast.walk(tree):
            if isinstance(node, ast.Import): imports.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom): imports.append(node.module or "")
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)): functions.append(node.name)
            elif isinstance(node, ast.ClassDef): classes.append(node.name)
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name): calls.append(node.func.id)
                elif isinstance(node.func, ast.Attribute): calls.append(node.func.attr)
        return ToolResult(True, {"syntax_valid":True,"imports":sorted(set(imports)),"functions":functions,"classes":classes,"calls":calls})
