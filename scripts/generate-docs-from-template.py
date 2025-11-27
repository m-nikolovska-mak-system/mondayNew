
#!/usr/bin/env python3
import yaml
from pathlib import Path

def generate_triggers(on):
    if isinstance(on, str): return f"- `{on}`"
    if isinstance(on, list): return "\n".join(f"- `{t}`" for t in on)
    if isinstance(on, dict): return "\n".join(f"- `{k}`" for k in on.keys())
    return "_No triggers defined._"

def generate_inputs(on):
    inputs = {}
    for key in ['workflow_call', 'workflow_dispatch']:
        if isinstance(on.get(key), dict):
            inputs.update(on[key].get('inputs', {}))
    if not inputs: return "_No inputs defined._"
    rows = ["| Name | Required | Description |", "| ---- | -------- | ----------- |"]
    for name, props in inputs.items():
        rows.append(f"| `{name}` | {'✅' if props.get('required') else '❌'} | {props.get('description','_No description_')} |")
    return "\n".join(rows)

workflow = yaml.safe_load(Path("ci-build-jar.yml").read_text())
template = Path("README_TEMPLATE.md").read_text()
filled = template.replace("{{TRIGGERS}}", generate_triggers(workflow.get("on", {})))
filled = filled.replace("{{INPUTS}}", generate_inputs(workflow.get("on", {})))
Path("README-ci-build-jar.md").write_text(filled)
