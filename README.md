# Code Migration Agent

A framework-independent OpenGAP agent for controlled Python code migration.

## Purpose

The agent provides four deterministic capabilities: source analysis, bounded Python migration, textual version comparison, and static migration validation. It is designed to make migration work auditable without coupling the core implementation to an LLM or a specific agent framework.

## Architecture

- `contracts/` defines the framework-independent tool interface.
- `core/` provides dynamic discovery, validation, execution, and structured responses.
- `tools/` contains domain implementations.
- `adapters/` provides thin portability interfaces for OpenAI, CrewAI, Claude Code, and Lyzr.
- `config/` reads runtime configuration exclusively from environment variables.
- `verification/` contains the readiness audit.

## Installation

Create a Python environment, install `requirements.txt`, and export the variables shown in `.env.example`. No credentials are required by the core implementation.

## Configuration

Runtime configuration is supplied through `CODE_MIGRATION_LOG_LEVEL`, `CODE_MIGRATION_MAX_FILE_BYTES`, `CODE_MIGRATION_MAX_FILES`, and `CODE_MIGRATION_WORKSPACE_ROOT`. Values are intentionally not populated with production defaults.

## Tools

1. `analyze-source` — parse Python and report imports, functions, classes, and calls.
2. `migrate-python` — apply explicit rules such as `rename-print-function` and `replace-xrange-with-range`.
3. `compare-versions` — produce a unified diff and line-change counts.
4. `validate-migration` — parse migrated Python and flag dynamic `eval`/`exec` calls.

## Skills

- `migration-analysis`
- `safe-python-migration`
- `migration-validation`

## Usage

Instantiate `ToolRegistry`, register the tools in `tools.ALL_TOOLS`, and pass it to `CodeMigrationAgent`. Call `agent.run(tool_name, inputs)` to obtain a structured `ToolResult`.

## Testing

Run `pytest -q`, then run `python verification/readiness_audit.py`.

## Portability

The core contract has no dependency on OpenAI, Claude, CrewAI, Lyzr, or another framework. The adapter classes expose a common invocation boundary; they do not claim external SDK integration unless a corresponding runtime is installed and tested.

## Limitations

The implementation is Python-focused. Static validation cannot establish behavioral equivalence, and textual comparison cannot establish semantic equivalence. Framework-specific migration details, dependency upgrades, binary assets, and runtime integration require project-specific validation.
