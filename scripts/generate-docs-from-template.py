#!/usr/bin/env python3
import yaml
import argparse
from pathlib import Path
from datetime import datetime
import sys

def generate_triggers(workflow):
    """Generate a clean, correct Markdown description of GitHub workflow triggers."""
    triggers = workflow.get("on", {})

    if not triggers:
        return "_This workflow has no triggers defined._"

    if isinstance(triggers, str):
        return f"- **`{triggers}`**"

    if isinstance(triggers, list):
        return "\n".join(f"- **`{t}`**" for t in triggers)

    if not isinstance(triggers, dict):
        return "_This workflow has no triggers defined._"

    lines = []
    for trigger, config in triggers.items():
        label = "workflow_call (reusable workflow)" if trigger == "workflow_call" else trigger

        if not config:
            lines.append(f"- **`{label}`**")
            continue

        if isinstance(config, dict):
            lines.append(f"- **`{label}`**")

            if "paths" in config:
                raw_paths = config["paths"]
                paths = raw_paths if isinstance(raw_paths, list) else [raw_paths]
                includes = [p for p in paths if not p.startswith("!")]
                excludes = [p[1:] for p in paths if p.startswith("!")]
                if includes:
                    lines.append(f"  - Includes: `{', '.join(includes)}`")
                if excludes:
                    lines.append(f"  - Excludes: `{', '.join(excludes)}`")

            if "branches" in config:
                b = config["branches"]
                branches = b if isinstance(b, list) else [b]
                lines.append(f"  - Branches: `{', '.join(branches)}`")

            if "types" in config:
                t = config["types"]
                types = t if isinstance(t, list) else [t]
                lines.append(f"  - Types: `{', '.join(types)}`")
        else:
            lines.append(f"- **`{label}`**")

    return "\n".join(lines) if lines else "_This workflow has no triggers defined._"


def generate_inputs(workflow):
    """Generate inputs table - works for both workflow_call and workflow_dispatch"""
    triggers = workflow.get('on', {})
    inputs = {}

    if isinstance(triggers, dict):
        wf_call = triggers.get('workflow_call')
        wf_dispatch = triggers.get('workflow_dispatch')

        if isinstance(wf_call, dict):
            inputs.update(wf_call.get('inputs', {}))
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
        default = f"`{default}`" if default != '' else '_not set_'
        desc = props.get('description', '_No description provided_')
        typ = f"`{props.get('type', 'string')}`"
        lines.append(f"| `{name}` | {typ} | {req} | {default} | {desc} |")

    return '\n'.join(lines)


def generate_outputs(workflow):
    """Generate outputs table - works for workflow_call"""
    triggers = workflow.get('on', {})
    outputs = {}

    if isinstance(triggers, dict):
        wf_call = triggers.get('workflow_call')
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

        sections.append(f"### 🔧 `{job_name}`")

        job_info = []
        if 'runs-on' in job:
            runs_on = job['runs-on']
            runs_on = ', '.join([f"`{r}`" for r in runs_on]) if isinstance(runs_on, list) else f"`{runs_on}`"
            job_info.append(f"**Runs on:** {runs_on}")

        if 'outputs' in job and isinstance(job['outputs'], dict):
            job_info.append(f"**Outputs:** {len(job['outputs'])} output(s)")

        if 'needs' in job:
            needs = job['needs'] if isinstance(job['needs'], list) else [job['needs']]
            job_info.append(f"**Depends on:** {', '.join([f'`{n}`' for n in needs])}")

        if job_info:
            sections.append('\n'.join(job_info))
            sections.append('')

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
                run_cmd = ''
                if 'run' in step:
                    run_text = step['run']
                    if isinstance(run_text, str):
                        run_text_clean = ' '.join(run_text.strip().split())
                        if len(run_text_clean) > 60:
                            run_cmd = '✅ Yes (see YAML)'
                        else:
                            run_text_clean = run_text_clean.replace('|', '\\|')
                            run_cmd = f'`{run_text_clean}`'
                    else:
                        run_cmd = '✅ Yes'
                action_display = f"`{action}`" if action else ''
                lines.append(f"| {name} | {action_display} | {run_cmd} |")
            sections.append('\n'.join(lines))
        else:
            sections.append('_This job has no steps defined._')

        sections.append('')

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

    return ' + '.join(workflow_types) if workflow_types else 'Standard Workflow'


def generate_docs_from_template(workflow_path, template_path, output_path):
    """Generate documentation by filling out a template"""
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            workflow = yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        print(f"❌ Error reading workflow: {e}")
        sys.exit(1)

    if not workflow or not isinstance(workflow, dict):
        print(f"❌ Invalid workflow file: {workflow_path}")
        sys.exit(1)

    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except Exception as e:
        print(f"❌ Error reading template: {e}")
        sys.exit(1)

    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            full_yaml = f.read().rstrip()
    except Exception as e:
        print(f"❌ Error reading full YAML: {e}")
        sys.exit(1)

    workflow_type = determine_workflow_type(workflow)
    generation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"✅ Generated documentation: {output_path}")
    except Exception as e:
        print(f"❌ Error writing output: {e}")
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate workflow documentation from template')
    parser.add_argument('--workflow', required=True, help='Path to workflow YAML file')
    parser.add_argument('--template', required=True, help='Path to template file')
    parser.add_argument('--output', required=True, help='Path to output README file')
    args = parser.parse_args()

