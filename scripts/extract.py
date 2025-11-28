#!/usr/bin/env python3
import yaml
import sys
from pathlib import Path

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def extract_workflow_call_section(workflow):
    """
    Returns the workflow_call section no matter if 'on' is parsed normally or as True.
    """
    on_section = workflow.get("on")
    
    # Normal case
    if isinstance(on_section, dict) and "workflow_call" in on_section:
        return on_section["workflow_call"]
    
    # Fallback if PyYAML parsed it strangely (e.g., {True: {...}})
    if isinstance(on_section, dict):
        for key, value in on_section.items():
            if isinstance(value, dict) and "workflow_call" in value:
                return value["workflow_call"]
    
    # Nothing found
    return {}

def extract_inputs(workflow):
    wf_call = extract_workflow_call_section(workflow)
    return wf_call.get("inputs", {})

def extract_outputs(workflow):
    wf_call = extract_workflow_call_section(workflow)
    return wf_call.get("outputs", {})

def format_inputs(inputs):
    """Convert inputs dict into Markdown string"""
    if not inputs:
        return "*(none)*"
    lines = []
    for name, data in inputs.items():
        lines.append(f"- {name}:")
        for k, v in data.items():
            lines.append(f"    {k}: {v}")
    return "\n".join(lines)

def format_outputs(outputs):
    """Convert outputs dict into Markdown string"""
    if not outputs:
        return "*(none)*"
    lines = []
    for name, data in outputs.items():
        lines.append(f"- {name}:")
        for k, v in data.items():
            lines.append(f"    {k}: {v}")
    return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract.py <workflow.yml> <output.md>")
        sys.exit(1)

    workflow_path = sys.argv[1]
    output_path = sys.argv[2]

    workflow = load_yaml(workflow_path)

    workflow_name = workflow.get("name", "Unnamed Workflow")
    inputs = extract_inputs(workflow)
    outputs = extract_outputs(workflow)

    inputs_md = format_inputs(inputs)
    outputs_md = format_outputs(outputs)

    # Load template
    template_path = Path("docs/workflow_readme.md.tpl")
    if not template_path.exists():
        print(f"Template not found: {template_path}")
        sys.exit(1)
    template_text = template_path.read_text(encoding="utf-8")

    # Replace placeholders
    final_md = (
        template_text
        .replace("{{WORKFLOW_NAME}}", workflow_name)
        .replace("{{INPUTS}}", inputs_md)
        .replace("{{OUTPUTS}}", outputs_md)
    )

    Path(output_path).write_text(final_md, encoding="utf-8")
    print(f"✅ README generated → {output_path}")
