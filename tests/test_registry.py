import pytest
from core.agent_core import ToolRegistry
from tools import ALL_TOOLS

def test_register_and_discover():
 r=ToolRegistry(); [r.register(t) for t in ALL_TOOLS]
 assert r.discover()==["analyze-source","compare-versions","migrate-python","validate-migration"]

def test_duplicate_registration():
 r=ToolRegistry(); r.register(ALL_TOOLS[0])
 with pytest.raises(ValueError): r.register(ALL_TOOLS[0])
