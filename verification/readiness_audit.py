from __future__ import annotations
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1]
REQUIRED_FILES=["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
REQUIRED_DIRS=["adapters","config","contracts","core","skills","tools","tests","verification"]

def sentence_count(text):
    return len([x for x in re.split(r"(?<=[.!?])\s+", text.strip()) if x])

def main():
    errors=[]
    for f in REQUIRED_FILES:
        if not (ROOT/f).is_file(): errors.append(f"Missing file: {f}")
    for d in REQUIRED_DIRS:
        if not (ROOT/d).is_dir(): errors.append(f"Missing directory: {d}")
    doc=(ROOT/"EXPLAINABILITY.md").read_text() if (ROOT/"EXPLAINABILITY.md").exists() else ""
    required=["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
    for heading in required:
        if doc.count(heading)!=1: errors.append(f"Required heading missing or duplicated: {heading}")
    for bad in ["## Inputs","## Decision","## Limits"]:
        if re.search(rf"^{re.escape(bad)}$",doc,re.M): errors.append(f"Conflicting heading found: {bad}")
    for heading in required:
        if heading in doc:
            section=doc.split(heading,1)[1].split("\n## ",1)[0]
            if sentence_count(section)<2: errors.append(f"Section needs at least two sentences: {heading}")
    if errors:
        print("READINESS AUDIT: FAIL")
        print("\n".join(f"- {e}" for e in errors)); return 1
    print("READINESS AUDIT: PASS")
    return 0
if __name__ == "__main__": sys.exit(main())
