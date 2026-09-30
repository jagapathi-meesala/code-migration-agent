from __future__ import annotations
from .portable_adapter import OpenAIAdapter, CrewAIAdapter, ClaudeCodeAdapter, LyzrAdapter, PortableAdapter

class AdapterRegistry:
    def __init__(self):
        self._adapters: dict[str, PortableAdapter] = {
            "openai": OpenAIAdapter(), "crewai": CrewAIAdapter(),
            "claude-code": ClaudeCodeAdapter(), "lyzr": LyzrAdapter(),
        }
    def names(self):
        return tuple(sorted(self._adapters))
    def get(self, name: str) -> PortableAdapter:
        if name not in self._adapters:
            raise KeyError(f"Unknown adapter: {name}")
        return self._adapters[name]
