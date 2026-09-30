from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Mapping

class PortableAdapter(ABC):
    name = "framework-independent"

    @abstractmethod
    def invoke(self, tool_name: str, inputs: Mapping[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

class OpenAIAdapter(PortableAdapter):
    name = "openai"
    def invoke(self, tool_name, inputs):
        return {"adapter": self.name, "tool": tool_name, "inputs": dict(inputs)}

class CrewAIAdapter(PortableAdapter):
    name = "crewai"
    def invoke(self, tool_name, inputs):
        return {"adapter": self.name, "tool": tool_name, "inputs": dict(inputs)}

class ClaudeCodeAdapter(PortableAdapter):
    name = "claude-code"
    def invoke(self, tool_name, inputs):
        return {"adapter": self.name, "tool": tool_name, "inputs": dict(inputs)}

class LyzrAdapter(PortableAdapter):
    name = "lyzr"
    def invoke(self, tool_name, inputs):
        return {"adapter": self.name, "tool": tool_name, "inputs": dict(inputs)}
