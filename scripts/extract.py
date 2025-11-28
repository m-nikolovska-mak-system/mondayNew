#!/usr/bin/env python3
import yaml
import sys

def main():
    # Get arguments
    workflow_file = sys.argv[1]  # e.g., .github/workflows/ci-build-jar.yml
    output_file = sys.argv[2]    # e.g., docs/ci-build-jar.md
    
    print(f"📖 Reading: {workflow_file}")
    
    # Load YAML
    with open(workflow_file, 'r') as f:
        workflow = yaml.safe_load(f)
    
    # Get workflow name
    workflow_name = workflow.get('name', 'Unnamed Workflow')
    print(f"✅ Workflow: {workflow_name}")
    
    # Get 'on' section
    on_section = workflow.get('on', {})
    
    # Extract inputs
    inputs = {}
    if 'workflow_call' in on_section and on_section['workflow_call']:
        inputs = on_section['workflow_call'].get('inputs', {})
    if 'workflow_dispatch' in on_section and on_section['workflow_dispatch']:
        inputs.update(on_section['workflow_dispatch'].get('inputs', {}))
    
    print(f"✅ Found {len(inputs)} input(s): {list(inputs.keys())}")
    
    # Extract outputs
    outputs = {}
    if 'workflow_call' in on_section and on_section['workflow_call']:
        outputs = on_section['workflow_call'].get('outputs', {})
    
    print(f"✅ Found {len(outputs)} output(s): {list(outputs.keys())}")
    
    # Format inputs table
    if inputs:
        inputs_text = "| Name | Type | Required | Default |\n"
        inputs_text += "| ---- | ---- | -------- | ------- |\n"
        for name, props in inputs.items():
            inp_type = props.get('type', 'string')
            required = 'Yes' if props.get('required', False) else 'No'
            default = props.get('default', '')
            inputs_text += f"| `{name}` | `{inp_type}` | {required} | `{default}` |\n"
    else:
        inputs_text = "_No inputs defined._"
    
    # Format outputs table
    if outputs:
        outputs_text = "| Name | Description |\n"
        outputs_text += "| ---- | ----------- |\n"
        for name, props in outputs.items():
            desc = props.get('description', '')
            outputs_text += f"| `{name}` | {desc} |\n"
    else:
        outputs_text = "_No outputs defined._"
    
    # Create README content
    readme = f"""# 📘 Workflow Documentation

Generated from: {workflow_name}

## 🧩 Inputs

{inputs_text}

## 🧪 Outputs

{outputs_text}
"""
    
    # Write output
    with open(output_file, 'w') as f:
        f.write(readme)
    
    print(f"✅ Created: {output_file}")

if __name__ == '__main__':
    main()
