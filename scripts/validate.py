#!/usr/bin/env python3
"""Validate the ASRI v0.1 knowledge core and cross-references."""

import json
from collections import Counter
from datetime import date
from pathlib import Path

import yaml

try:
    import jsonschema
except ImportError:  # Minimal local fallback; CI installs the full validator.
    jsonschema = None


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION ERROR: {message}")


schema = json.loads((ROOT / "schema/knowledge-object.schema.json").read_text())
objects = yaml.safe_load((ROOT / "knowledge_objects/core-v0.1.yaml").read_text())["objects"]
sources = yaml.safe_load((ROOT / "sources/source-registry.yaml").read_text())["sources"]

object_ids = [item["id"] for item in objects]
source_ids = [item["id"] for item in sources]

if len(object_ids) < 30:
    fail(f"at least 30 Knowledge Objects required; found {len(object_ids)}")
if len(object_ids) != len(set(object_ids)):
    fail("duplicate Knowledge Object id")
if len(source_ids) != len(set(source_ids)):
    fail("duplicate source id")

known_objects = set(object_ids)
known_sources = set(source_ids)

for item in objects:
    if jsonschema is not None:
        jsonschema.validate(item, schema)
    else:
        missing_fields = set(schema["required"]) - set(item)
        if missing_fields:
            fail(f"{item.get('id', '<unknown>')} missing fields: {sorted(missing_fields)}")
        if item["status"] not in schema["properties"]["status"]["enum"]:
            fail(f"{item['id']} has invalid status")
        if item["evidence_level"] not in schema["properties"]["evidence_level"]["enum"]:
            fail(f"{item['id']} has invalid evidence level")
    missing_sources = set(item["source_ids"]) - known_sources
    missing_related = set(item.get("related_ids", [])) - known_objects
    if missing_sources:
        fail(f"{item['id']} has missing sources: {sorted(missing_sources)}")
    if missing_related:
        fail(f"{item['id']} has missing related objects: {sorted(missing_related)}")
    if item["id"] in item.get("related_ids", []):
        fail(f"{item['id']} relates to itself")
    if item["status"] == "stable" and len(item["source_ids"]) < 2:
        fail(f"{item['id']} is stable but has fewer than two sources")
    if date.fromisoformat(item["last_reviewed"]) > date.today():
        fail(f"{item['id']} has a future review date")

status = Counter(item["status"] for item in objects)
evidence = Counter(item["evidence_level"] for item in objects)
print(f"OK: {len(objects)} objects, {len(sources)} sources")
print("status:", dict(sorted(status.items())))
print("evidence:", dict(sorted(evidence.items())))
