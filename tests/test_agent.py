from core.agent_core import CodeMigrationAgent, ToolRegistry
from tools import ALL_TOOLS

def agent():
 r=ToolRegistry()
 for t in ALL_TOOLS: r.register(t)
 return CodeMigrationAgent(r)

def test_capabilities():
 assert agent().capabilities()["tools"] == ["analyze-source","compare-versions","migrate-python","validate-migration"]

def test_run_valid_tool():
 result=agent().run("analyze-source",{"source":"def f():\n    return 1\n"})
 assert result.ok and "f" in result.data["functions"]

def test_unknown_tool():
 try: agent().run("missing",{})
 except KeyError: assert True
 else: assert False
