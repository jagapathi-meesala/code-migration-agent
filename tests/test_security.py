from tools import ALL_TOOLS

def get(name): return next(x for x in ALL_TOOLS if x.metadata.name==name)

def test_missing_field_rejected():
 r=get("analyze-source").run({})
 assert not r.ok and r.error["type"]=="validation_error"

def test_unknown_field_rejected():
 r=get("analyze-source").run({"source":"x=1","secret":"bad"})
 assert not r.ok

def test_unsafe_construct_detected():
 r=get("validate-migration").run({"source":"exec('x')"})
 assert r.ok and r.data["issues"][0]["type"]=="unsafe_dynamic_execution"
