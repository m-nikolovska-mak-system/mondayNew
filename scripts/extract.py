#!/usr/bin/env python3
import yaml
import sys

def main():
    # Get arguments
    workflow_file = sys.argv[1]  # e.g., .github/workflows/ci-build-jar.yml
    output_file = sys.argv[2]    # e.g., docs/README-ci-build-jar.md
    
    print(f"📖 Reading: {workflow_file}")
    
    # Load YAML
    with open(workflow_file, 'r') as f:
        workflow = yaml.safe_load(f)
    
    # Debug: print entire workflow structure
    print(f"🔍 Full workflow keys: {list(workflow.keys())}")
    print(f"🔍 Raw keys with repr:")
    for key in workflow.keys():
        print(f"   - {repr(key)}: {type(workflow[key])}")
    print()
    
    # Try to find 'on' key (might have weird characters)
    on_key = None
    for key in workflow.keys():
        if 'on' in key.lower():
            on_key = key
            print(f"🔍 Found 'on'-like key: {repr(key)}")
            break
    
    if on_key is None:
        print("❌ Could not find 'on' key in workflow!")
        on_key = 'on'  # fallback
    
    # Get workflow name
    workflow_name = workflow.get('name', 'Unnamed Workflow')
    print(f"✅ Workflow: {workflow_name}")
    
    # Get 'on' section
    on_section = workflow.get(on_key, {})
    print(f"🔍 'on' section type: {type(on_section)}")
    print(f"🔍 'on' section content: {on_section}")
    print(f"🔍 Triggers: {list(on_section.keys()) if isinstance(on_section, dict) else 'NOT A DICT'}")
    print()
    
    # Extract inputs
    inputs = {}
    
    # Check workflow_call
    if 'workflow_call' in on_section:
        wf_call = on_section['workflow_call']
        print(f"🔍 workflow_call type: {type(wf_call)}")
        print(f"🔍 workflow_call value: {wf_call}")
        
        if wf_call is not None and isinstance(wf_call, dict):
            call_inputs = wf_call.get('inputs', {})
            print(f"🔍 workflow_call inputs: {call_inputs}")
            if call_inputs:
                inputs.update(call_inputs)
    
    # Check workflow_dispatch
    if 'workflow_dispatch' in on_section:
        wf_dispatch = on_section['workflow_dispatch']
        if wf_dispatch is not None and isinstance(wf_dispatch, dict):
            dispatch_inputs = wf_dispatch.get('inputs', {})
            if dispatch_inputs:
                inputs.update(dispatch_inputs)
    
    print(f"✅ Found {len(inputs)} input(s): {list(inputs.keys())}")
    
    # Extract outputs
    outputs = {}
    
    if 'workflow_call' in on_section:
        wf_call = on_section['workflow_call']
        print(f"🔍 workflow_call for outputs type: {type(wf_call)}")
        
        if wf_call is not None and isinstance(wf_call, dict):
            call_outputs = wf_call.get('outputs', {})
            print(f"🔍 workflow_call outputs: {call_outputs}")
            if call_outputs:
                outputs.update(call_outputs)
    
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
