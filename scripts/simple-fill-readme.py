#!/usr/bin/env python3
import argparse
import yaml
from datetime import datetime
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate README from workflow YAML and template")
    parser.add_argument("--workflow", required=True, help="Path to workflow YAML")
    parser.add_argument("--template", required=True, help="Path to template file")
    parser.add_argument("--output", required=True, help="Path to save the generated README")
    args = parser.parse_args()

    # Load workflow YAML
    try:
        with open(args.workflow, "r", encoding="utf-8") as f:
            workflow = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Workflow file not found: {args.workflow}")
        sys.exit(1)

    workflow_name = workflow.get("name", "Unnamed Workflow")
    inputs = workflow.get("on", {}).get("workflow_dispatch", {}).get("inputs", {})

    # Extract placeholders from workflow inputs (use defaults if not defined)
    title = inputs.get("title", {}).get("default", workflow_name)
    description = inputs.get("description", {}).get("default", "Workflow documentation")
    version = inputs.get("version", {}).get("default", "1.0")
    date = datetime.now().strftime("%Y-%m-%d")

    data = {
        "{{TITLE}}": title,
        "{{DESCRIPTION}}": description,
        "{{VERSION}}": version,
        "{{DATE}}": date,
    }

    # Read template
    try:
        with open(args.template, "r", encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"❌ Template file not found: {args.template}")
        sys.exit(1)

    # Replace placeholders
    readme_content = template_content
    for placeholder, value in data.items():
        readme_content = readme_content.replace(placeholder, value)

    # Write output
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Debug info
    print(f"✅ README created: {args.output}")
    print(f"   TITLE: {title}")
    print(f"   DESCRIPTION: {description}")
    print(f"   VERSION: {version}")
    print(f"   DATE: {date}")
    print(f"   Size: {len(readme_content)} characters")

if __name__ == "__main__":
    main()
