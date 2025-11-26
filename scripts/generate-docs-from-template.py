#!/usr/bin/env python3
import yaml
import argparse
from pathlib import Path

def generate_triggers(workflow):
    """Generate triggers section"""
    triggers = workflow.get('on', {})
    
    # Handle both dict and string cases
    if isinstance(triggers, str):
        return f"- `{triggers}`"
    elif isinstance(triggers, dict):
        lines = []
        for trigger in triggers.keys():
            lines.append(f"- `{trigger}`")
        return '\n'.join(lines) if lines else '_None_'
    
    return '_None_'

def generate_inputs(workflow):
    """Generate inputs table"""
    triggers = workflow.get('on', {})
    
    # Try to find inputs in workflow_call
    workflow_call = None
    if isinstance(triggers, dict):
        workflow_call = triggers.get('workflow_call', {})
    
    if not workflow_call:
        return '_None_'
    
    inputs = workflow_call.get('inputs', {})
    
    if not inputs:
        return '_None_'
    
    lines = [
        "| name | type | required | default | description |",
        "| --- | --- | --- | --- | --- |"
    ]
    
    for name, props in inputs.items():
        req = "yes" if props.get('required', False) else "no"
        default = str(props.get('default', ''))
        desc = props.get('description', '')
        typ = props.get('type', 'string')
        lines.append(f"| {name} | {typ} | {req} | {default} | {desc} |")
    
    return '\n'.join(lines)

def generate_outputs(workflow):
    """Generate outputs table"""
    triggers = workflow.get('on', {})
    
    # Try to find outputs in workflow_call
    workflow_call = None
    if isinstance(triggers, dict):
        workflow_call = triggers.get('workflow_call', {})
    
    if not workflow_call:
        return '_None_'
    
    outputs = workflow_call.get('outputs', {})
    
    if not outputs:
        return '_None_'
    
    lines = [
        "| name | description |",
        "| --- | --- |"
    ]
    
    for name, props in outputs.items():
        desc = props.get('description', '')
        lines.append(f"| {name} | {desc} |")
    
    return '\n'.join(lines)

def generate_secrets(workflow):
    """Generate secrets table"""
    triggers = workflow.get('on', {})
    
    # Try to find secrets in workflow_call
    workflow_call = None
    if isinstance(triggers, dict):
        workflow_call = triggers.get('workflow_call', {})
    
    if not workflow_call:
        return '_None_'
    
    secrets = workflow_call.get('secrets', {})
    
    if not secrets:
        return '_None_'
    
    lines = [
        "| name | required | description |",
        "| --- | --- | --- |"
    ]
    
    for name, props in secrets.items():
        req = "yes" if props.get('required', False) else "no"
        desc = props.get('description', '')
        lines.append(f"| {name} | {req} | {desc} |")
    
    return '\n'.join(lines)

def generate_jobs(workflow):
    """Generate jobs section"""
    jobs = workflow.get('jobs', {})
    
    if not jobs:
        return '_None_'
    
    sections = []
    
    for job_name, job in jobs.items():
        sections.append(f"### {job_name}")
        steps = job.get('steps', [])
        
        if steps:
            lines = [
                "| name | action | run |",
                "| --- | --- | --- |"
            ]
            
            for step in steps:
                name = step.get('name', '')
                action = step.get('uses', '')
                run = '`run` command' if 'run' in step else ''
                lines.append(f"| {name} | {action} | {run} |")
            
            sections.append('\n'.join(lines))
        else:
            sections.append('_No steps defined_')
    
    return '\n\n'.join(sections)

def generate_docs_from_template(workflow_path, template_path, output_path):
    """Generate documentation by filling out a template"""
    
    # Parse workflow YAML
    with open(workflow_path, 'r') as f:
        workflow = yaml.safe_load(f)
    
    # Debug: Print the parsed structure
    print(f"📋 Parsing workflow: {workflow_path}")
    print(f"   Triggers found: {list(workflow.get('on', {}).keys())}")
    
    # Read template
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Read full YAML content
    with open(workflow_path, 'r') as f:
        full_yaml = f.read().rstrip()
    
    # Generate all sections
    replacements = {
        '{{WORKFLOW_NAME}}': workflow.get('name', Path(workflow_path).stem),
        '{{WORKFLOW_FILE}}': Path(workflow_path).name,
        '{{TRIGGERS}}': generate_triggers(workflow),
        '{{INPUTS}}': generate_inputs(workflow),
        '{{OUTPUTS}}': generate_outputs(workflow),
        '{{SECRETS}}': generate_secrets(workflow),
        '{{JOBS}}': generate_jobs(workflow),
        '{{FULL_YAML}}': full_yaml
    }
    
    # Fill out template
    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)
    
    # Ensure output directory exists
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Write output
    with open(output_path, 'w') as f:
        f.write(result)
    
    print(f"✅ Generated documentation: {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate workflow documentation from template')
    parser.add_argument('--workflow', required=True, help='Path to workflow YAML file')
    parser.add_argument('--template', required=True, help='Path to template file')
    parser.add_argument('--output', required=True, help='Path to output README file')
    args = parser.parse_args()
    
    generate_docs_from_template(args.workflow, args.template, args.output)
