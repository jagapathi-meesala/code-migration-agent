# Rules

1. Validate every tool input before processing it.
2. Never execute user-supplied source code during static analysis or migration.
3. Apply only explicitly supported migration rules.
4. Report unsupported rules instead of silently guessing.
5. Do not embed credentials, API keys, passwords, or runtime secrets in source or configuration.
6. Treat syntax validation and textual comparison as evidence, not proof of behavioral equivalence.
7. Keep framework-specific integrations outside the core migration logic.
