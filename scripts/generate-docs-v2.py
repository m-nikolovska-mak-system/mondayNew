import yaml
from pathlib import Path
from datetime import datetime

WORKFLOWS_DIR = Path(".github/workflows")
DOCS_DIR = Path("docs/workflows")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

def build_header(name):
    return f"# 📝 {name}\n\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n"

def build_triggers(triggers) -> str:
    doc = "## ⚡ Triggers\n\n"
    doc += "| Event | Details |\n|-------|---------|\n"

    if not triggers:
        doc += "| – | No triggers defined |\n\n"
        return doc

    if isinstance(triggers, dict):
        for event, config in triggers.items():
            # Special case: reusable workflow
            if event == "workflow_call":
                doc += "| `workflow_call` | Reusable workflow (called from other workflows) |\n"
                continue

            # Special case: manual dispatch
            if event == "workflow_dispatch":
                doc += "| `workflow_dispatch` | Manually triggered from the Actions tab |\n"
                continue

            details = []
            if isinstance(config, dict):
                branches = config.get("branches")
                if isinstance(branches, list):
                    details.append(f"Branches: `{', '.join(branches)}`")
                paths = config.get("paths")
                if isinstance(paths, list):
                    details.append(f"Paths: `{', '.join(paths)}`")

            if details:
                doc += f"| `{event}` | {'<br>'.join(details)} |\n"
            else:
                doc += f"| `{event}` | No filters |\n"

    elif isinstance(triggers, list):
        for event in triggers:
            doc += f"| `{event}` | Standard trigger |\n"

    else:
        doc += f"| `{triggers}` | Standard trigger |\n"

    return doc + "\n"


def build_workflow_call_io(triggers) -> str:
    # Only care if this workflow uses `workflow_call`
    if not isinstance(triggers, dict) or "workflow_call" not in triggers:
        return ""

    call_cfg = triggers["workflow_call"]
    doc = ""

    # Inputs
    inputs = call_cfg.get("inputs") or {}
    if inputs:
        doc += "## 📥 Inputs\n\n"
        doc += "| Name | Type | Required | Default | Description |\n"
        doc += "|------|------|----------|---------|-------------|\n"
        for name, cfg in inputs.items():
            typ = cfg.get("type", "string")
            required = "yes" if cfg.get("required", False) else "no"
            default = cfg.get("default", "—")
            desc = cfg.get("description", "")
            doc += f"| `{name}` | `{typ}` | {required} | `{default}` | {desc} |\n"
        doc += "\n"

    # Outputs
    outputs = call_cfg.get("outputs") or {}
    if outputs:
        doc += "## 📤 Outputs\n\n"
        doc += "| Name | Description | Value |\n"
        doc += "|------|-------------|-------|\n"
        for name, cfg in outputs.items():
            desc = cfg.get("description", "")
            value = cfg.get("value", "")
            doc += f"| `{name}` | {desc} | `{value}` |\n"
        doc += "\n"

    return doc



def build_jobs(jobs):
    doc = "## 🔨 Jobs\n\n"
    for job_name, job_data in jobs.items():
        doc += f"### `{job_name}`\n\n"
        doc += f"**Runner:** `{job_data.get('runs-on', 'unknown')}`\n\n"
        if "outputs" in job_data:
            doc += "**Job Outputs:**\n\n"
            for k, v in job_data["outputs"].items():
                doc += f"- `{k}`: `{v}`\n"
            doc += "\n"
        doc += "**Steps:**\n\n"
        for i, step in enumerate(job_data.get("steps", []), start=1):
            name = step.get("name", "Unnamed step")
            doc += f"{i}. **{name}**\n"
            if "uses" in step:
                doc += f"   - 📦 Action: `{step['uses']}`\n"
            if "run" in step:
                doc += f"   - 💻 Run: `{step['run']}`\n"
            if "with" in step:
                doc += f"   - ⚙️ Config:\n"
                for k, v in step["with"].items():
                    doc += f"     - `{k}`: `{v}`\n"
            doc += "\n"
    return doc

def generate_doc(workflow_path):
    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)
    basename = workflow_path.stem
    doc_path = DOCS_DIR / f"README-{basename}.md"
    name = workflow.get("name", basename)
    doc = build_header(name)
    doc += "## Overview\n\n"
    doc += f"**Workflow File:** `{workflow_path}`\n\n"
    doc += build_triggers(workflow.get("on", {}))
    doc += build_jobs(workflow.get("jobs", {}))
    doc += "---\n\n*This documentation is auto-generated. Do not edit manually.*\n"
    doc_path.write_text(doc)
    print(f"✅ Generated: {doc_path}")

IGNORED_FILES = {"workflow-docs.yml", "workflow-docs.yaml"}

def main():
    workflow_files = list(WORKFLOWS_DIR.glob("*.yml")) + list(WORKFLOWS_DIR.glob("*.yaml"))
    for wf in workflow_files:
        if wf.name in IGNORED_FILES:
            continue
        generate_doc(wf)


if __name__ == "__main__":
    main()
