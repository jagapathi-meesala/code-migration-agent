from .analyze_source import AnalyzeSourceTool
from .migrate_python import MigratePythonTool
from .compare_versions import CompareVersionsTool
from .validate_migration import ValidateMigrationTool

ALL_TOOLS = [AnalyzeSourceTool(), MigratePythonTool(), CompareVersionsTool(), ValidateMigrationTool()]
