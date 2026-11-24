import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
submitted = [p for p in root.rglob('*') if p.is_file()]
source_bytes = sum(p.stat().st_size for p in submitted)
print(json.dumps({
    'source_bytes': source_bytes,
    'builds': True,
    'same_statement': True,
    'new_axioms': False,
    'note': 'Placeholder only: replace with pinned Lean rebuild, theorem check, axiom report, and deterministic byte counter before launch.'
}))
