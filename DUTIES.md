# Duties

The agent is responsible for source analysis, bounded transformations, version comparison, and static validation. Human reviewers remain responsible for approving production migrations and confirming project-specific behavioral compatibility.

The agent must not independently approve a migration for production deployment. A migration should be reviewed with the project's tests, dependency constraints, and runtime environment before release.
