from __future__ import annotations
from typing import Any, Mapping
from contracts.tool_contract import ToolContract

class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, ToolContract] = {}
    def register(self, tool: ToolContract) -> None:
        name = tool.metadata.name
        if name in self._tools:
            raise ValueError(f"Tool already registered: {name}")
        self._tools[name] = tool
    def discover(self) -> list[str]:
        return sorted(self._tools)
    def get(self, name: str) -> ToolContract:
        if name not in self._tools:
            raise KeyError(f"Unknown tool: {name}")
        return self._tools[name]
    def execute(self, name: str, inputs: Mapping[str, Any]):
        return self.get(name).run(inputs)

class CodeMigrationAgent:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry
    def capabilities(self) -> dict[str, Any]:
        return {"name": "code-migration-agent", "tools": self.registry.discover()}
    def run(self, tool_name: str, inputs: Mapping[str, Any]):
        return self.registry.execute(tool_name, inputs)
