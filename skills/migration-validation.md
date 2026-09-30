# Migration Validation

## Purpose
Provide a static safety check after migration.

## Inputs
A non-empty Python source string.

## Processing
The tool parses the source and inspects the AST for unsafe dynamic execution calls.

## Outputs
A validity flag and structured issue list.

## Limitations
Static checks do not prove runtime correctness, dependency compatibility, or behavioral equivalence.

## Expected Behavior
Syntax errors and unsafe dynamic execution constructs are surfaced rather than hidden.
