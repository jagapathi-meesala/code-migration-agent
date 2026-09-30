---
name: migration-validation
description: Validate migrated Python source for syntax integrity and migration safety conditions.
---

# Migration Validation

## Purpose
Validate migrated Python source using deterministic static checks.

## Inputs
Migrated Python source code.

## Processing
Parse the source using Python AST processing and identify syntax errors and selected unsafe dynamic execution patterns.

## Outputs
Validation status and structured validation issues.

## Limitations
Static validation cannot prove runtime behavior, integration correctness, or semantic equivalence.

## Expected Behavior
Valid source passes structural checks unless configured safety conditions are detected; invalid source produces structured validation information.
