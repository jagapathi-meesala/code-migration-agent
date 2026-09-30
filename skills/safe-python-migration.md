# Safe Python Migration

## Purpose
Apply explicit, bounded source transformations to Python code.

## Inputs
Python source and a list of named migration rules.

## Processing
The implementation parses source with AST and applies only supported transformations. Unsupported rules are collected in the output instead of being guessed.

## Outputs
Migrated source, applied rules, and unsupported rules.

## Limitations
Only the documented migration rules are supported and no source code is executed.

## Expected Behavior
A valid source remains parseable after supported transformations, while malformed source is rejected through structured error handling.
