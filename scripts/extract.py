#!/usr/bin/env python3
import yaml
import sys

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def extract_inputs(workflow):
    """Return dict of workflow_call.inputs"""
    try:
        return workflow["on"]["workflow_call"].get("inputs", {})
    except Exception:
        return {}

def extract_outputs(workflow):
    """Return dict of workflow_call.outputs"""
    try:
        return workflow["on"]["workflow_call"].get("outputs", {})
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
