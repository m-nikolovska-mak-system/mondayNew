#!/usr/bin/env python3
import yaml
import sys

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def extract_inputs(workflow):
    """Safely get workflow_call.inputs even if YAML structure varies."""
    try:
        on_section = workflow.get("on", {})

        # Sometimes PyYAML parses a single trigger as a dict
        if isinstance(on_section, dict):
            wf_call = on_section.get("workflow_call", {})
            return wf_call.get("inputs", {}) or {}

        # Sometimes "on" is parsed as a list of events
        if isinstance(on_section, list):
            for item in on_section:
                if isinstance(item, dict) and "workflow_call" in item:
                    return item["workflow_call"].get("inputs", {}) or {}

        return {}

    except Exception:
        return {}


def extract_outputs(workflow):
    """Safely get workflow_call.outputs even if YAML structure varies."""
    try:
        on_section = workflow.get("on", {})

        if isinstance(on_section, dict):
            wf_call = on_section.get("workflow_call", {})
            return wf_call.get("outputs", {}) or {}

        if isinstance(on_section, list):
            for item in on_section:
                if isinstance(item, dict) and "workflow_call" in item:
                    return item["workflow_call"].get("outputs", {}) or {}

        return {}

    except Exception:
        return {}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract.py <workflow.yml>")
        sys.exit(1)

    path = sys.argv[1]
    workflow = load_yaml(path)

    inputs = extract_inputs(workflow)
    outputs = extract_outputs(workflow)

    print("=== INPUTS ===")
    for name, data in inputs.items():
        print(f"- {name}:")
        for k, v in data.items():
            print(f"    {k}: {v}")

    print("\n=== OUTPUTS ===")
    for name, data in outputs.items():
        print(f"- {name}:")
        for k, v in data.items():
            print(f"    {k}: {v}")
