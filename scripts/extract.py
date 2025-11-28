#!/usr/bin/env python3
import yaml
import sys

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_on_section(workflow):
    # Handle both correct YAML and the "True:" parsing bug
    if "on" in workflow:
        return workflow["on"]
    if True in workflow:
        return workflow[True]
    return {}

def extract_inputs(workflow):
    on_section = get_on_section(workflow)
    return on_section.get("workflow_call", {}).get("inputs", {})

def extract_outputs(workflow):
    on_section = get_on_section(workflow)
    return on_section.get("workflow_call", {}).get("outputs", {})

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract.py <workflow.yml>")
        sys.exit(1)

    path = sys.argv[1]
    workflow = load_yaml(path)

    print("DEBUG STRUCTURE:")
    print(workflow)
    print("---------------")

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
