#!/usr/bin/env python3
import yaml
import argparse
from pathlib import Path

def generate_triggers(workflow):
    """Generate triggers section with better formatting"""
    triggers = workflow.get('on', {})
    
    if not triggers:
        return '_This workflow has no triggers defined._'
    
    if isinstance(triggers, str):
        return f"- `{triggers}`"
    
    if isinstance(triggers, list):
        return '\n'.join([f"- `{t}`" for t in triggers])
    
    # Handle dict triggers
    lines = []
    for trigger, config in triggers.items():
        if config is None or config == {}:
            lines.append(f"- **`{trigger}`**")
        elif isinstance(config, dict):
            lines.append(f"- **`{trigger}`**")
            # Add trigger details
            if 'paths' in config:
                lines.append(f"  - Paths: `{', '.join(config['paths'])}`")
            if 'branches' in config:
                lines.append(f"  - Branches: `{', '.join(config['branches'])}`")
        else:
            lines.append(f"- **`{trigger}`**")
    
    return '\n'.join(lines) if lines else '_This workflow has no triggers defined._'

def generate_inputs(workflow):
    """Generate inputs table with better handling"""
    triggers = workflow.get('on', {})
    
    # Handle workflow_call inputs
    if isinstance(triggers, dict):
        workflow_call = triggers.get('workflow_call', {})
        inputs = workflow_call.get('inputs', {})
    else:
        inputs = {}
    
    if not inputs:
        return '_This workflow does not accept any inputs._'
    
    lines = [
        "| Name | Type | Required | Default | Description |",
        "| ---- | ---- | -------- | ------- | ----------- |"
    ]
    
    for name, props in inputs.items():
        req = "✅ Yes" if props.get('required', False) else "❌ No"
        default = f"`{props.get('default', '')}`" if props.get('default', '') else '_not set_'
        desc = props.get('description', '_No description provided_')
        typ = f"`{props.get('type', 'string')}`"
        lines.append(f"| `{name}` | {typ} | {req} | {default} | {desc} |")
    
    return '\n'.join(lines)

def generate_outputs(workflow):
    """Generate outputs table with better formatting"""
    triggers = workflow.get('on', {})
    
    if isinstance(triggers, dict):
        workflow_call = triggers.get('workflow_call', {})
        outputs = workflow_call.get('outputs', {})
    else:
        outputs = {}
    
    if not outputs:
        return '_This workflow does not expose any outputs._'
    
    lines = [
        "| Name | Description | Value |",
        "| ---- | ----------- | ----- |"
    ]
    
    for name, props in outputs.items():
        desc = props.get('description', '_No description provided_')
        value = props.get('value', '_not specified_')
        # Truncate long values for readability
        if len(str(value)) > 50:
            value = f"`{str(value)[:47]}...`"
        else:
            value = f"`{value}`"
        lines.append(f"| `{name}` | {desc} | {value} |")
    
    return '\n'.join(lines)

def generate_secrets(workflow):
    """Generate secrets table with better formatting"""
    triggers = workflow.get('on', {})
    
    if isinstance(triggers, dict):
        workflow_call = triggers.get('workflow_call', {})
        secrets = workflow_call.get('secrets', {})
    else:
        secrets = {}
    
    if not secrets:
        return '_This workflow does not require any secrets._'
    
    lines = [
        "| Name | Required | Description |",
        "| ---- | -------- | ----------- |"
    ]
    
    for name, props in secrets.items():
        req = "✅ Yes" if props.get('required', False) else "❌ No"
        desc = props.get('description', '_No description provided_')
        lines.append(f"| `{name}` | {req} | {desc} |")
    
    return '\n'.join(lines)

def generate_jobs(workflow):
    """Generate jobs section with improved formatting"""
    jobs = workflow.get('jobs', {})
    
    if not jobs:
        return '_This workflow has no jobs defined._'
    
    sections = []
    
    for job_name, job in jobs.items():
        # Job header
        sections.append(f"### 🔧 `{job_name}`")
        
        # Add job-level info if available
        job_info = []
        if 'runs-on' in job:
            job_info.append(f"**Runs on:** `{job['runs-on']}`")
        if 'outputs' in job:
            job_info.append(f"**Outputs:** {len(job['outputs'])} output(s)")
        if 'needs' in job:
            needs = job['needs'] if isinstance(job['needs'], list) else [job['needs']]
            job_info.append(f"**Depends on:** {', '.join([f'`{n}`' for n in needs])}")
        
        if job_info:
            sections.append('\n'.join(job_info))
            sections.append('')  # blank line
        
        # Steps table
        steps = job.get('steps', [])
        
        if steps:
            lines = [
                "| Step | Uses | Run Command |",
                "| ---- | ---- | ----------- |"
            ]
            
            for i, step in enumerate(steps, 1):
                name = step.get('name', f'_Step {i}_')
                action = step.get('uses', '')
                
                # Handle run commands
                run_cmd = ''
                if 'run' in step:
                    run_text = step['run']
                    # Truncate long run commands
                    if isinstance(run_text, str) and len(run_text) > 50:
                        run_cmd = '✅ Yes (see YAML)'
                    elif isinstance(run_text, str):
                        run_cmd = f'`{run_text}`'
                    else:
                        run_cmd = '✅ Yes'
                
                action_display = f"`{action}`" if action else ''
                lines.append(f"| {name} | {action_display} | {run_cmd} |")
            
            sections.append('\n'.join(lines))
        else:
            sections.append('_This job has no steps defined._')
        
        sections.append('')  # blank line between jobs
    
    return '\n\n'.join(sections)

def generate_docs_from_template(workflow_path, template_path, output_path):
    """Generate documentation by filling out a template"""
    
    # Parse workflow YAML
    with open(workflow_path, 'r') as f:
        workflow = yaml.safe_load(f)
    
    # Read template
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Read full YAML content
    with open(workflow_path, 'r') as f:
        full_yaml = f.read().rstrip()
    
    # Generate workflow type
    triggers = workflow.get('on', {})
    workflow_type = 'Reusable Workflow' if isinstance(triggers, dict) and 'workflow_call' in triggers else 'Standard Workflow'
    
    # Generate all sections
    replacements = {
        '{{WORKFLOW_NAME}}': workflow.get('name', Path(workflow_path).stem),
        '{{WORKFLOW_FILE}}': Path(workflow_path).name,
        '{{WORKFLOW_TYPE}}': workflow_type,
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
