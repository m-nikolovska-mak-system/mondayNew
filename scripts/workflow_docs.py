import yaml
from pathlib import Path
from datetime import datetime

WORKFLOWS_DIR = Path(".github/workflows")
DOCS_DIR = Path("docs/workflows")
DOCS_DIR.mkdir(parents=True, exist_ok=True)

IGNORED_FILES = {"workflow-docs.yml", "workflow-docs.yaml"}


def build_header(name: str) -> str:
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return (
        f"# 📝 {name}\n\n"
        f"**Generated:** {ts}\n\n"
        "---\n\n"
    )


def build_overview(path: Path) -> str:
    return (
        "## Overview\n\n"
        f"**Workflow File:** `{path}`\n\n"
    )


def build_triggers(triggers) -> str:
    doc = "## ⚡ Triggers\n\n"
    doc += "| Event | Details |\n|-------|---------|\n"

    if not triggers:
        doc += "| – | No triggers defined |\n\n"
        return doc

    if isinstance(triggers, dict):
        for event, config in triggers.items():
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


def build_jobs(jobs: dict) -> str:
    doc = "## 🔨 Jobs\n\n"
    if not jobs:
        return doc + "_No jobs defined._\n\n"

    for job_name, job_data in jobs.items():
        doc += f"### `{job_name}`\n\n"
        runner = job_data.get("runs-on", "unknown")
        doc += f"**Runner:** `{runner}`\n\n"

        # Job outputs (if any)
        outputs = job_data.get("outputs")
        if outputs:
            doc += "**Job Outputs:**\n\n"
            for k, v in outputs.items():
                doc += f"- `{k}`: `{v}`\n"
            doc += "\n"

        # Steps
        steps = job_data.get("steps", [])
        doc += "**Steps:**\n\n"
        for i, step in enumerate(steps, start=1):
            name = step.get("name", f"Step {i}")
            doc += f"{i}. **{name}**\n"
            if "uses" in step:
                doc += f"   - 📦 Action: `{step['uses']}`\n"
            if "run" in step:
                # keep run short-ish in docs
                run_cmd = str(step["run"]).strip()
                run_cmd = run_cmd.replace("\n", " ")[:120]
                doc += f"   - 💻 Run: `{run_cmd}...`\n"
            if "with" in step:
                doc += f"   - ⚙️ Config:\n"
                for k, v in step["with"].items():
                    doc += f"     - `{k}`: `{v}`\n"
            doc += "\n"

    return doc


def generate_doc(workflow_path: Path) -> None:
    try:
        with workflow_path.open() as f:
            workflow = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Failed to parse {workflow_path}: {e}")
        return

    if not workflow:
        print(f"⚠️ Empty or invalid workflow: {workflow_path}")
        return

    basename = workflow_path.stem
    doc_path = DOCS_DIR / f"README-{basename}.md"
    name = workflow.get("name", basename)

    doc = ""
    doc += build_header(name)
    doc += build_overview(workflow_path)
    doc += build_triggers(workflow.get("on"))
    doc += build_jobs(workflow.get("jobs", {}))
    doc += "---\n\n*This documentation is auto-generated. Do not edit manually.*\n"

    doc_path.write_text(doc, encoding="utf-8")
    print(f"✅ Generated: {doc_path}")


def main():
    workflow_files = list(WORKFLOWS_DIR.glob("*.yml")) + list(WORKFLOWS_DIR.glob("*.yaml"))

    for wf in workflow_files:
        if wf.name in IGNORED_FILES:
            continue
        generate_doc(wf)


if __name__ == "__main__":
    main()
