#!/usr/bin/env python3
import argparse
import yaml
from datetime import datetime
from pathlib import Path
import sys


def format_section(title, data_dict):
    """Return clean markdown list or placeholder text."""
    if not data_dict:
        return "_None_"

    lines = []
    for key, val in data_dict.items():
        if isinstance(val, dict):
            default = val.get("default", "")
            desc = val.get("description", "")
            t = val.get("type", "")
            extra = []

            if desc:
                extra.append(f"desc: {desc}")
            if t:
                extra.append(f"type: {t}")
            if default:
                extra.append(f"default: {default}")

            meta = f" ({', '.join(extra)})" if extra else ""
            lines.append(f"- **{key}**{meta}")
        else:
            lines.append(f"- **{key}**")

    return "\n".join(lines)


def extract_triggers(on_section):
    """
    Convert every trigger into clean Markdown.
    Covers:
      - push
      - pull_request
      - workflow_dispatch
      - workflow_call
      - schedule
      - release
      - ANY other event GitHub supports
    """
    if not on_section:
        return "_None_"

    lines = []
    for event, value in on_section.items():
        if value in (None, {}, []) or isinstance(value, bool):
            # simple triggers: "push:", "release:"
            lines.append(f"- **{event}**")
        elif isinstance(value, list):
            # e.g. schedule: [ cron: "..." ]
            lines.append(f"- **{event}**: list ({len(value)} items)")
        elif isinstance(value, dict):
            # e.g. push: { branches: [...], tags: [...] }
            details = ", ".join(value.keys())
            lines.append(f"- **{event}** ({details})")
        else:
            lines.append(f"- **{event}**")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--template", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    # Load workflow YAML
    try:
        workflow = yaml.safe_load(Path(args.workflow).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"❌ Workflow not found: {args.workflow}")
        sys.exit(1)

    # Base metadata
    name = workflow.get("name", "Unnamed Workflow")
    date = datetime.now().strftime("%Y-%m-%d")

    # Extract triggers
    on_section = workflow.get("on", {})
    triggers_md = extract_triggers(on_section)

    # Extract inputs (dispatch + call)
    inputs = {}
    dispatch = on_section.get("workflow_dispatch", {})
    if isinstance(dispatch, dict):
        inputs.update(dispatch.get("inputs", {}))

    call = on_section.get("workflow_call", {})
    if isinstance(call, dict):
        inputs.update(call.get("inputs", {}))

    inputs_md = format_section("Inputs", inputs)

    # Outputs
    outputs = call.get("outputs", {}) if isinstance(call, dict) else {}
    outputs_md = format_section("Outputs", outputs)

    # Secrets
    secrets = call.get("secrets", {}) if isinstance(call, dict) else {}
    secrets_md = format_section("Secrets", secrets)

    # Read template
    try:
        template = Path(args.template).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"❌ Template not found: {args.template}")
        sys.exit(1)

    # Replace placeholders
    final = (
        template
        .replace("{{TITLE}}", name)
        .replace("{{DATE}}", date)
        .replace("{{TRIGGERS}}", triggers_md)
        .replace("{{INPUTS}}", inputs_md)
        .replace("{{OUTPUTS}}", outputs_md)
        .replace("{{SECRETS}}", secrets_md)
    )

    # Write output
    Path(args.output).write_text(final, encoding="utf-8")
    print(f"✅ README generated → {args.output}")


if __name__ == "__main__":
    main()
