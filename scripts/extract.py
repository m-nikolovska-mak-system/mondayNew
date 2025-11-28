#!/usr/bin/env python3
import yaml
import sys
from pathlib import Path

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def extract_inputs(workflow):
    try:
        return workflow["on"]["workflow_call"].get("inputs", {})
    except Exception:
        return {}

def extract_outputs(workflow):
    try:
        return workflow["on"]["workflow_call"].get("outputs", {})
    except Exception:
        return {}

def format_inputs(inputs):
    if not inputs:
        return "*(none)*"

    lines = []
    for name, data in inputs.items():
        lines.append(f"- **{name}**")
        for k, v in data.items():
            lines.append(f"  - {k}: `{v}`")
    return "\n".join(lines)

def format_outputs(outputs):
    if not outputs:
        return "*(none)*"

    lines = []
    for name, data in outputs.items():
        lines.append(f"- **{name}**")
        for k, v in data.items():
            lines.append(f"  - {k}: `{v}`")
    return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract.py <workflow.yml> <output.md>")
        sys.exit(1)

    workflow_path = sys.argv[1]
    output_path = sys.argv[2]

    workflow = load_yaml(workflow_path)

    name = workflow.get("name", "Unnamed Workflow")
    inputs = extract_inputs(workflow)
    outputs = extract_outputs(workflow)

    inputs_md = format_inputs(inputs)
    outputs_md = format_outputs(outputs)

    # Load template
    template_path = Path("templates/workflow_readme.md.tpl")
    template_text = template_path.read_text(encoding="utf-8")

    final_md = (
        template_text
        .replace("{{WORKFLOW_NAME}}", name)
        .replace("{{INPUTS}}", inputs_md)
        .replace("{{OUTPUTS}}", outputs_md)
    )

    Path(output_path).write_text(final_md, encoding="utf-8")

    print(f"README generated → {output_path}")
