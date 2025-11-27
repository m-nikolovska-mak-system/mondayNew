#!/usr/bin/env python3
import yaml
import argparse
from pathlib import Path
from datetime import datetime

def generate_triggers(workflow):
    """Generate a clean, correct Markdown description of GitHub workflow triggers."""
    triggers = workflow.get("on", {})

    # Debug
    print(f"[DEBUG] generate_triggers: type(on)={type(triggers)}, value={triggers}")

    # --- CASE 0: missing or empty ---
    if not triggers:
        return "_This workflow has no triggers defined._"

    # --- CASE 1: string ---
    # on: push
    if isinstance(triggers, str):
        return f"- **`{triggers}`**"

    # --- CASE 2: list ---
    # on: [push, pull_request]
    if isinstance(triggers, list):
        return "\n".join(f"- **`{t}`**" for t in triggers)

    # --- CASE 3: invalid type ---
    if not isinstance(triggers, dict):
        return "_This workflow has no triggers defined._"

    # --- CASE 4: dict ---
    # on:
    #   push:
    #     branches: [...]
    #   pull_request:
    #     paths: [...]

    lines = []

    for trigger, config in triggers.items():

        # Human-friendly name for workflow_call
        label = "workflow_call (reusable workflow)" if trigger == "workflow_call" else trigger

        # CASE: config is empty or None
        if not config:
            lines.append(f"- **`{label}`**")
            continue

        # Only dict configs contain detailed filters
        if isinstance(config, dict):
            lines.append(f"- **`{label}`**")

            # Paths
            if "paths" in config:
                raw_paths = config["paths"]
                paths = raw_paths if isinstance(raw_paths, list) else [raw_paths]

                includes = [p for p in paths if not p.startswith("!")]
                excludes = [p[1:] for p in paths if p.startswith("!")]

                if includes:
                    lines.append(f"  - Includes: `{', '.join(includes)}`")
                if excludes:
                    lines.append(f"  - Excludes: `{', '.join(excludes)}`")

            # Branches
            if "branches" in config:
                b = config["branches"]
                branches = b if isinstance(b, list) else [b]
                lines.append(f"  - Branches: `{', '.join(branches)}`")

            # Types
            if "types" in config:
                t = config["types"]
                types = t if isinstance(t, list) else [t]
                lines.append(f"  - Types: `{', '.join(types)}`")

        else:
            # Weird case: config is not dict
            lines.append(f"- **`{label}`**")

    return "\n".join(lines) if lines else "_This workflow has no triggers defined._"


def generate_inputs(workflow):
    """Generate inputs table - works for both workflow_call and workflow_dispatch"""
    triggers = workflow.get('on', {})
    inputs = {}

    # Debug to see structure of triggers
    print(f"[DEBUG] generate_inputs: type(on)={type(triggers)}, value={triggers}")

    if isinstance(triggers, dict):
        wf_call = triggers.get('workflow_call')
        wf_dispatch = triggers.get('workflow_dispatch')
        print(f"[DEBUG] generate_inputs: workflow_call={type(wf_call)}, workflow_dispatch={type(wf_dispatch)}")

        # Reusable workflow inputs
        if isinstance(wf_call, dict):
            inputs.update(wf_call.get('inputs', {}))
        # Manual dispatch inputs
        if isinstance(wf_dispatch, dict):
            inputs.update(wf_dispatch.get('inputs', {}))

    if not inputs:
        return '_This workflow does not accept any inputs._'

    lines = [
        "| Name | Type | Required | Default | Description |",
        "| ---- | ---- | -------- | ------- | ----------- |"
    ]

    for name, props in inputs.items():
        if not isinstance(props, dict):
            continue

        req = "✅ Yes" if props.get('required', False) else "❌ No"
        default = props.get('default', '')

        if default != '':
            if isinstance(default, str):
                default = f"`{default}`"
            else:
                default = f"`{str(default)}`"
        else:
            default = '_not set_'

        desc = props.get('description', '_No description provided_')
        typ = f"`{props.get('type', 'string')}`"
        lines.append(f"| `{name}` | {typ} | {req} | {default} | {desc} |")

    return '\n'.join(lines)


def generate_outputs(workflow):
    """Generate outputs table - works for workflow_call"""
    triggers = workflow.get('on', {})
    outputs = {}

    # Debug to see structure of triggers
    print(f"[DEBUG] generate_outputs: type(on)={type(triggers)}, value={triggers}")

    if isinstance(triggers, dict):
        wf_call = triggers.get('workflow_call')
        print(f"[DEBUG] generate_outputs: workflow_call={type(wf_call)}")
        if isinstance(wf_call, dict):
            outputs = wf_call.get('outputs', {})

    if not outputs:
        return '_This workflow does not expose any outputs._'

    lines = [
        "| Name | Description | Value |",
        "| ---- | ----------- | ----- |"
    ]

    for name, props in outputs.items():
        if not isinstance(props, dict):
            continue

        desc = props.get('description', '_No description provided_')
        value = props.get('value', '_not specified_')

        if isinstance(value, str):
            if len(value) > 60:
                value = f"`{value[:57]}...`"
            else:
                value = f"`{value}`"
        else:
            value = f"`{str(value)}`"

        lines.append(f"| `{name}` | {desc} | {value} |")

    return '\n'.join(lines)


def generate_secrets(workflow):
    """Generate secrets table - works for workflow_call"""
    triggers = workflow.get('on', {})
    secrets = {}
    
    if isinstance(triggers, dict) and 'workflow_call' in triggers:
        workflow_call = triggers['workflow_call']
        if isinstance(workflow_call, dict):
            secrets = workflow_call.get('secrets', {})
    
    if not secrets:
        return '_This workflow does not require any secrets._'
    
    lines = [
        "| Name | Required | Description |",
        "| ---- | -------- | ----------- |"
    ]
    
    for name, props in secrets.items():
        if not isinstance(props, dict):
            continue
            
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
        if not isinstance(job, dict):
            continue
            
        # Job header
        sections.append(f"### 🔧 `{job_name}`")
        
        # Add job-level info if available
        job_info = []
        if 'runs-on' in job:
            runs_on = job['runs-on']
            if isinstance(runs_on, list):
                runs_on = ', '.join([f"`{r}`" for r in runs_on])
            else:
                runs_on = f"`{runs_on}`"
            job_info.append(f"**Runs on:** {runs_on}")
            
        if 'outputs' in job and isinstance(job['outputs'], dict):
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
                if not isinstance(step, dict):
                    continue
                    
                name = step.get('name', f'_Step {i}_')
                action = step.get('uses', '')
                
                # Handle run commands
                run_cmd = ''
                if 'run' in step:
                    run_text = step['run']
                    # Handle multi-line run commands
                    if isinstance(run_text, str):
                        # Remove extra whitespace and newlines
                        run_text_clean = ' '.join(run_text.strip().split())
                        if len(run_text_clean) > 60:
                            run_cmd = '✅ Yes (see YAML)'
                        else:
                            # Escape pipe characters that might break markdown tables
                            run_text_clean = run_text_clean.replace('|', '\\|')
                            run_cmd = f'`{run_text_clean}`'
                    else:
                        run_cmd = '✅ Yes'
                
                action_display = f"`{action}`" if action else ''
                lines.append(f"| {name} | {action_display} | {run_cmd} |")
            
            sections.append('\n'.join(lines))
        else:
            sections.append('_This job has no steps defined._')
        
        sections.append('')  # blank line between jobs
    
    return '\n\n'.join(sections)

def determine_workflow_type(workflow):
    """Determine if workflow is reusable, dispatch, standard, etc."""
    triggers = workflow.get('on', {})
    
    if not isinstance(triggers, dict):
        return 'Standard Workflow'
    
    workflow_types = []
    
    if 'workflow_call' in triggers:
        workflow_types.append('Reusable Workflow')
    if 'workflow_dispatch' in triggers:
        workflow_types.append('Manual Dispatch')
    if any(t in triggers for t in ['push', 'pull_request', 'schedule', 'release']):
        workflow_types.append('Automated')
    
    if not workflow_types:
        return 'Standard Workflow'
    
    return ' + '.join(workflow_types)

def generate_docs_from_template(workflow_path, template_path, output_path):
    """Generate documentation by filling out a template"""
    
    # Parse workflow YAML
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            workflow = yaml.load(f, Loader=yaml.FullLoader)
    except yaml.YAMLError as e:
        print(f"❌ Error parsing YAML: {e}")
        return
    except FileNotFoundError:
        print(f"❌ Workflow file not found: {workflow_path}")
        return
    except Exception as e:
        print(f"❌ Unexpected error reading workflow: {e}")
        return
    
    # after loading workflow and before using it
    if not workflow or not isinstance(workflow, dict):
        print(f"❌ Empty or invalid YAML file: {workflow_path}")
        return

    print(f"[DEBUG] Loaded workflow file: {workflow_path}")
    print(f"[DEBUG] Top-level keys: {list(workflow.keys())}")
    print(f"[DEBUG] 'on' section raw value: {workflow.get('on')}")


    
    # Read template
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
        print(f"💡 Make sure the template exists at: {template_path}")
        return
    except Exception as e:
        print(f"❌ Error reading template: {e}")
        return

    
    # Read template
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"❌ Template file not found: {template_path}")
        print(f"💡 Make sure the template exists at: {template_path}")
        return
    except Exception as e:
        print(f"❌ Error reading template: {e}")
        return
    
    # Read full YAML content
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            full_yaml = f.read().rstrip()
    except Exception as e:
        print(f"❌ Error reading workflow file for full content: {e}")
        return
    
    # Generate workflow type
    workflow_type = determine_workflow_type(workflow)
    
    # Generate current date
    generation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
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
        '{{FULL_YAML}}': full_yaml,
        '{{GENERATION_DATE}}': generation_date
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
