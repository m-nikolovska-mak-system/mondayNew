import yaml
import sys
import os
from pathlib import Path

def generate_workflow_doc(workflow_path):
    with open(workflow_path, 'r') as f:
        workflow = yaml.safe_load(f)
    
    basename = Path(workflow_path).stem
    doc_path = f"docs/README-{basename}.md"
    
    # Start with template header
    doc = f"# 📝 {workflow.get('name', basename)} Workflow\n\n"
    doc += "## Overview\n\n"
    
    # Add workflow description if available
    if 'name' in workflow:
        doc += f"**Workflow Name:** `{workflow['name']}`\n\n"
    
    # Trigger information
    doc += "## Triggers\n\n"
    if 'on' in workflow:
        triggers = workflow['on']
        if isinstance(triggers, dict):
            for trigger, config in triggers.items():
                if trigger == 'workflow_call':
                    doc += f"- `{trigger}` (Reusable workflow)\n"
                elif isinstance(config, dict):
                    doc += f"- `{trigger}`\n"
                    if 'branches' in config:
                        doc += f"  - Branches: `{', '.join(config['branches'])}`\n"
                    if 'paths' in config:
                        doc += f"  - Paths: `{', '.join(config['paths'])}`\n"
                else:
                    doc += f"- `{trigger}`\n"
        else:
            doc += f"- `{triggers}`\n"
    
    doc += "\n"
    
    # Inputs (for reusable workflows)
    if 'on' in workflow and isinstance(workflow['on'], dict):
        if 'workflow_call' in workflow['on']:
            call_config = workflow['on']['workflow_call']
            if 'inputs' in call_config:
                doc += "## Inputs\n\n"
                doc += "| Name | Type | Required | Default | Description |\n"
                doc += "|------|------|----------|---------|-------------|\n"
                for name, config in call_config['inputs'].items():
                    required = '✅' if config.get('required', False) else '❌'
                    input_type = config.get('type', 'string')
                    default = config.get('default', '-')
                    description = config.get('description', '-')
                    doc += f"| `{name}` | `{input_type}` | {required} | `{default}` | {description} |\n"
                doc += "\n"
            
            if 'outputs' in call_config:
                doc += "## Outputs\n\n"
                doc += "| Name | Description |\n"
                doc += "|------|-------------|\n"
                for name, config in call_config['outputs'].items():
                    description = config.get('description', '-')
                    doc += f"| `{name}` | {description} |\n"
                doc += "\n"
    
    # Jobs
    if 'jobs' in workflow:
        doc += "## Jobs\n\n"
        for job_name, job_config in workflow['jobs'].items():
            doc += f"### `{job_name}`\n\n"
            if 'runs-on' in job_config:
                doc += f"**Runner:** `{job_config['runs-on']}`\n\n"
            
            if 'steps' in job_config:
                doc += "**Steps:**\n\n"
                for i, step in enumerate(job_config['steps'], 1):
                    step_name = step.get('name', f'Step {i}')
                    doc += f"{i}. **{step_name}**\n"
                    if 'uses' in step:
                        doc += f"   - Uses: `{step['uses']}`\n"
                    if 'run' in step:
                        run_preview = step['run'].split('\n')[0][:60]
                        doc += f"   - Runs: `{run_preview}...`\n"
                doc += "\n"
    
    # Usage example for reusable workflows
    if 'on' in workflow and isinstance(workflow['on'], dict):
        if 'workflow_call' in workflow['on']:
            doc += "## Usage Example\n\n"
            doc += "```yaml\n"
            doc += "jobs:\n"
            doc += f"  call-{basename}:\n"
            doc += f"    uses: ./.github/workflows/{Path(workflow_path).name}\n"
            if 'workflow_call' in workflow['on'] and 'inputs' in workflow['on']['workflow_call']:
                doc += "    with:\n"
                for input_name in workflow['on']['workflow_call']['inputs'].keys():
                    doc += f"      {input_name}: value\n"
            doc += "```\n\n"
    
    doc += "---\n\n"
    doc += "*This documentation is auto-generated. Do not edit manually.*\n"
    
    # Write the documentation
    with open(doc_path, 'w') as f:
        f.write(doc)
    
    print(f"✅ Generated: {doc_path}")
    return doc_path

if __name__ == "__main__":
    workflows = sys.argv[1:]
    generated = []
    for wf in workflows:
        if wf.strip():
            try:
                doc = generate_workflow_doc(wf.strip())
                generated.append(doc)
            except Exception as e:
                print(f"❌ Error processing {wf}: {e}")
    
    # Save list of generated files
    with open('generated_docs.txt', 'w') as f:
        f.write('\n'.join(generated))
