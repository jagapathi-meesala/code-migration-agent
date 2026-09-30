---
name: migration-analysis
description: Analyze Python source code for migration targets, compatibility issues, and transformation requirements.
---

# Migration Analysis

## Purpose
Analyze Python source before migration so imports, functions, classes, and calls are visible to the caller.

## Inputs
A non-empty Python source string.

## Processing
The tool parses the source with Python's AST module and extracts migration-relevant structural elements without executing the program.

## Outputs
Syntax status, imports, function names, class names, and called function or method names.

## Limitations
The analysis is Python-focused and does not resolve runtime imports or prove semantic behavior.

## Expected Behavior
Invalid Python returns a structured syntax error; valid Python returns deterministic structural data.
