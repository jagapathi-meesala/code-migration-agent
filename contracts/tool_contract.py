from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping

class ToolValidationError(ValueError):
    pass

@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: Mapping[str, Any]
    limitations: tuple[str, ...] = field(default_factory=tuple)

@dataclass
class ToolResult:
    ok: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: dict[str, Any] | None = None

class ToolContract:
    metadata: ToolMetadata

    def validate(self, inputs: Mapping[str, Any]) -> None:
        schema = self.metadata.input_schema
        if not isinstance(inputs, Mapping):
            raise ToolValidationError("Input must be an object")
        required = schema.get("required", [])
        for key in required:
            if key not in inputs:
                raise ToolValidationError(f"Missing required field: {key}")
        if schema.get("additionalProperties") is False:
            allowed = set(schema.get("properties", {}))
            unknown = set(inputs) - allowed
            if unknown:
                raise ToolValidationError(f"Unexpected fields: {sorted(unknown)}")

    def execute(self, inputs: Mapping[str, Any]) -> ToolResult:
        raise NotImplementedError

    def run(self, inputs: Mapping[str, Any]) -> ToolResult:
        try:
            self.validate(inputs)
            return self.execute(inputs)
        except (ToolValidationError, ValueError, TypeError) as exc:
            return ToolResult(ok=False, error={"type": "validation_error", "message": str(exc)})
        except Exception as exc:  # defensive boundary; no secret data is returned
            return ToolResult(ok=False, error={"type": "execution_error", "message": str(exc)})
