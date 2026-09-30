# Explainability

## Inputs and Data Sources

The agent accepts source code, explicit migration rules, or before-and-after text as tool inputs. Its data source is the user-provided source text and configuration supplied through validated tool arguments; the core implementation does not silently fetch external project data.

### Input Requirements

Source inputs must be non-empty strings, and migration rules must be a list of strings. The comparison tool accepts two text versions, while validation operates on one Python source string.

### Failure Handling

Missing fields, unexpected fields, wrong types, and empty source values produce structured validation errors. Syntax errors are reported with location information when Python parsing fails.

## Decision and Reasoning

Migration decisions are made from explicit rules supplied by the caller rather than inferred from hidden defaults. For supported transformations, the agent parses Python into an abstract syntax tree and changes only the named construct, while unsupported rules are reported without modification.

### Rules Applied

`rename-print-function` renames Python `print` calls to `log`, and `replace-xrange-with-range` renames `xrange` calls to `range`. Validation marks source as invalid when static inspection finds `eval` or `exec`, and comparison computes additions and deletions from a unified textual diff.

### Expected Outputs

Successful tools return structured data containing the requested analysis, migrated source, diff statistics, or validation findings. Failures are represented with an error type and message so callers can distinguish validation failures from execution failures.

## Limits and Constraints

Static parsing does not prove that migrated code behaves identically at runtime. The implementation does not execute user source, does not support binary migration, and does not claim compatibility with a target framework merely because an adapter interface exists.

### Constraints

Only explicitly supported migration rules are applied, and unsupported rules remain visible in the result. Project dependencies, generated code, runtime configuration, external services, and framework-specific APIs require additional project-level verification.

### Worked Example

Given `print('hello')` and the rule `rename-print-function`, the migration produces `log('hello')` without executing the source. A subsequent validation run parses the resulting source and reports whether static safety checks pass.
