from tools import ALL_TOOLS

def get(name): return next(x for x in ALL_TOOLS if x.metadata.name==name)

def test_analyze_source():
 r=get("analyze-source").run({"source":"import os\nclass A: pass\ndef f(): return os.getcwd()"})
 assert r.ok and r.data["imports"] == ["os"] and r.data["classes"] == ["A"]

def test_migrate_python():
 r=get("migrate-python").run({"source":"print('x')\nxrange(2)","rules":["rename-print-function","replace-xrange-with-range"]})
 assert r.ok and "log('x')" in r.data["migrated_source"] and "range(2)" in r.data["migrated_source"]

def test_compare():
 r=get("compare-versions").run({"before":"a\n","after":"b\n"})
 assert r.ok and r.data["additions"]==1 and r.data["deletions"]==1

def test_validate():
 r=get("validate-migration").run({"source":"eval('2+2')"})
 assert r.ok and not r.data["valid"]
