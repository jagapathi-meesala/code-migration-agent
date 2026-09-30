from adapters.registry import AdapterRegistry

def test_adapters():
 r=AdapterRegistry()
 assert r.names()==("claude-code","crewai","lyzr","openai")
 assert r.get("openai").invoke("x",{"a":1})["adapter"]=="openai"
