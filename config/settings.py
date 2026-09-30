from __future__ import annotations
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    log_level: str
    max_file_bytes: int
    max_files: int
    workspace_root: str

def _required(name: str) -> str:
    value = os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Required environment variable is missing: {name}")
    return value.strip()

def load_settings() -> Settings:
    try:
        max_file_bytes = int(_required("CODE_MIGRATION_MAX_FILE_BYTES"))
        max_files = int(_required("CODE_MIGRATION_MAX_FILES"))
    except ValueError as exc:
        raise RuntimeError("CODE_MIGRATION_MAX_FILE_BYTES and CODE_MIGRATION_MAX_FILES must be integers") from exc
    if max_file_bytes <= 0 or max_files <= 0:
        raise RuntimeError("File limits must be positive")
    return Settings(
        log_level=_required("CODE_MIGRATION_LOG_LEVEL"),
        max_file_bytes=max_file_bytes,
        max_files=max_files,
        workspace_root=_required("CODE_MIGRATION_WORKSPACE_ROOT"),
    )
