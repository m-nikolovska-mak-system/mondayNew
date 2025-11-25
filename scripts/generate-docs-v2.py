import yaml
from pathlib import Path
from datetime import datetime

WORKFLOWS_DIR = Path(".github/workflows")
DOCS_DIR = Path("docs/workflows")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

def build_header(name):
    return f"# 📝 {name}\n\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n"

def build_triggers(triggers):
    doc = "## ⚡ Triggers\n\n"
    doc += "| Event | Details |\n|-------|---------|\n"
    if isinstance(triggers, dict):
        for event, config in triggers.items():
            details = []
            if isinstance(config, dict):
                if "branches" in config:
                    details.append(f"Branches: `{', '.join(config['branches'])}`")
                if "paths" in config:
                    details.append(f"Paths: `{', '.join(config['paths'])}`")
            doc += f"| `{event}` | {'<br>'.join(details) if details else 'No filters'} |\n"
    elif isinstance(triggers, list):
        for event in triggers:
            doc += f"| `{event}` | Standard trigger |\n"
    else:
        doc += f"| `{triggers}` | Standard trigger |\n"
    return doc + "\n"

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

def main():
    for wf in WORKFLOWS_DIR.glob("*.yml"):
        generate_doc(wf)
    for wf in WORKFLOWS_DIR.glob("*.yaml"):
        generate_doc(wf)

if __name__ == "__main__":
    main()
