
#!/usr/bin/env python3
import yaml
from pathlib import Path
from datetime import datetime

# ------------------------------
# Helper functions
# ------------------------------

def generate_triggers(on):
    if isinstance(on, str):
        return f"- `{on}`"
    if isinstance(on, list):
        return "\n".join(f"- `{t}`" for t in on)
    if isinstance(on, dict):
        return "\n".join(f"- `{k}`" for k in on.keys())
    return "_No triggers defined._"

def generate_inputs(on):
    inputs = {}
    for key in ['workflow_call', 'workflow_dispatch']:
        if isinstance(on.get(key), dict):
            inputs.update(on[key].get('inputs', {}))
    rows = ["| Name | Required | Description |", "| ---- | -------- | ----------- |"]
    if not inputs:
        rows.append("| `example_input` | ❌ | _No description provided_ |")
    else:
        for name, props in inputs.items():
            rows.append(f"| `{name}` | {'✅' if props.get('required') else '❌'} | {props.get('description','_No description_')} |")
    return "\n".join(rows)

def generate_outputs(on):
    wf_call = on.get('workflow_call', {})
    outputs = wf_call.get('outputs', {}) if isinstance(wf_call, dict) else {}
    rows = ["| Name | Description | Value |", "| ---- | ----------- | ----- |"]
    if not outputs:
        rows.append("| `example_output` | _No description provided_ | `_not specified_` |")
    else:
        for name, props in outputs.items():
            desc = props.get('description', '_No description provided_')
            value = props.get('value', '_not specified_')
            rows.append(f"| `{name}` | {desc} | `{value}` |")
    return "\n".join(rows)

def generate_secrets(on):
    wf_call = on.get('workflow_call', {})
    secrets = wf_call.get('secrets', {}) if isinstance(wf_call, dict) else {}
    rows = ["| Name | Required | Description |", "| ---- | -------- | ----------- |"]
    if not secrets:
        rows.append("| `example_secret` | ❌ | _No description provided_ |")
    else:
        for name, props in secrets.items():
            req = "✅" if props.get('required') else "❌"
            desc = props.get('description', '_No description provided_')
            rows.append(f"| `{name}` | {req} | {desc} |")
    return "\n".join(rows)

def generate_jobs(workflow):
    jobs = workflow.get('jobs', {})
    if not jobs:
        return "_No jobs defined._"
    sections = []
    for job_name, job in jobs.items():
        sections.append(f"### `{job_name}`")
        runs_on = job.get('runs-on', '')
        if runs_on:
            sections.append(f"**Runs on:** `{runs_on}`")
        steps = job.get('steps', [])
        if steps:
            rows = ["| Step | Uses | Run Command |", "| ---- | ---- | ----------- |"]
            for i, step in enumerate(steps, 1):
                name = step.get('name', f'Step {i}')
                uses = step.get('uses', '')
                run_cmd = step.get('run', '')
                run_display = f"`{run_cmd}`" if run_cmd else ''
                rows.append(f"| {name} | `{uses}` | {run_display} |")
            sections.append("\n".join(rows))
    return "\n\n".join(sections)

# ------------------------------
# Main function
# ------------------------------

def generate_doc(yaml_file):
    workflow = yaml.safe_load(Path(yaml_file).read_text())
    name = workflow.get('name', 'Unnamed Workflow')
    on = workflow.get('on', {})
    doc = f"""# 📋 Overview
This document provides comprehensive documentation for the **{name}** workflow.

🎯 **Triggers**
{generate_triggers(on)}

📥 **Inputs**
{generate_inputs(on)}

📤 **Outputs**
{generate_outputs(on)}

🔐 **Secrets**
{generate_secrets(on)}

💼 **Jobs**
{generate_jobs(workflow)}

📄 **Full Workflow YAML**
```yaml
{Path(yaml_file).read_text()}
