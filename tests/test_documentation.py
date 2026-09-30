from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_explainability_structure():
 text=(ROOT/"EXPLAINABILITY.md").read_text()
 for h in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]: assert text.count(h)==1
 for h in ["## Inputs","## Decision","## Limits"]: assert f"\n{h}\n" not in text
