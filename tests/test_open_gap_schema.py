from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def test_manifest_core_schema_constraints():
 data=yaml.safe_load((ROOT/"agent.yaml").read_text())
 assert data["spec_version"]=="0.1.0"
 assert data["name"]=="code-migration-agent"
 assert set(data)-{"spec_version","name","version","description","license","skills","tools","tags","metadata"}==set()
 assert all(isinstance(x,str) and x.endswith(('',)) for x in data["skills"])
 assert all(Path(ROOT/"skills"/f"{x}.md").is_file() for x in data["skills"])
 assert all(Path(ROOT/"tools"/f"{x.replace('-','_')}.py").is_file() for x in data["tools"])
