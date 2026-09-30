---
name: safe-python-migration
description: Apply conservative Python source transformations for explicitly supported migration rules.
---

# Safe Python Migration

## Purpose
Apply deterministic Python source transformations without executing the source program.

## Inputs
Python source code and an explicit list of migration rules.

## Processing
Parse the source using Python AST processing and apply only explicitly supported transformation rules.

## Outputs
Migrated source, applied rules, and unsupported rules.

## Limitations
Only supported deterministic transformations are applied. Runtime behavior and semantic equivalence are not guaranteed.

## Expected Behavior
Supported rules are applied deterministically; unsupported rules are reported instead of being guessed.
