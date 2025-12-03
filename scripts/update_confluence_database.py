import requests
import json
import sys
import os

CONFLUENCE_BASE = os.getenv("CONFLUENCE_BASE")
CONFLUENCE_USER = os.getenv("CONFLUENCE_USER")
CONFLUENCE_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")

DB_PAGE_ID = os.getenv("CONFLUENCE_DB_PAGE_ID")

def get_database_definition():
    url = f"{CONFLUENCE_BASE}/api/v2/pages/{DB_PAGE_ID}"
    res = requests.get(url, auth=(CONFLUENCE_USER, CONFLUENCE_TOKEN))
    res.raise_for_status()

    db = res.json().get("database", {})
    return db.get("fields", {})


def get_database_rows():
    url = f"{CONFLUENCE_BASE}/api/v2/pages/{DB_PAGE_ID}/database/rows"
    res = requests.get(url, auth=(CONFLUENCE_USER, CONFLUENCE_TOKEN))
    res.raise_for_status()
    return res.json()["results"]


def add_or_update_row(workflow_name, readme_page_id):
    fields = get_database_definition()

    # We must use the actual internal field IDs
    workflow_field = None
    readme_field = None

    for f in fields:
        if f["name"] == "Workflow Name":
            workflow_field = f["id"]
        if f["name"] == "README Page":
            readme_field = f["id"]

    if not workflow_field or not readme_field:
        raise ValueError("Database columns 'Workflow Name' or 'README Page' not found.")

    rows = get_database_rows()

    # ----- UPDATE if exists -----
    for row in rows:
        props = row["properties"]
        if props.get(workflow_field, {}).get("value") == workflow_name:
            row_id = row["id"]
            url = f"{CONFLUENCE_BASE}/api/v2/database/rows/{row_id}"
            payload = {
                "properties": {
                    workflow_field: {"value": workflow_name},
                    readme_field: {"value": [{"id": readme_page_id}]}
                }
            }
            requests.put(url, auth=(CONFLUENCE_USER, CONFLUENCE_TOKEN), json=payload)
            print("Updated existing row.")
            return

    # ----- INSERT if not found -----
    url = f"{CONFLUENCE_BASE}/api/v2/pages/{DB_PAGE_ID}/database/rows"
    payload = {
        "properties": {
            workflow_field: {"value": workflow_name},
            readme_field: {"value": [{"id": readme_page_id}]}
        }
    }
    requests.post(url, auth=(CONFLUENCE_USER, CONFLUENCE_TOKEN), json=payload)
    print("Inserted new row.")

if __name__ == "__main__":
    workflow_name = sys.argv[1]
    readme_page_id = sys.argv[2]
    add_or_update_row(workflow_name, readme_page_id)
