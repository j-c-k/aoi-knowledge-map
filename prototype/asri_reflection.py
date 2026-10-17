#!/usr/bin/env python3
"""Deterministic ASRI relevance baseline. It does not diagnose or decide."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9áéíóöőúüű\s]", " ", text).replace("  ", " ").strip()


def load_data() -> tuple[dict[str, dict], dict]:
    objects = yaml.safe_load((ROOT / "knowledge_objects/core-v0.1.yaml").read_text())["objects"]
    profiles = yaml.safe_load((ROOT / "prototype/retrieval-profiles.yaml").read_text())
    return {item["id"]: item for item in objects}, profiles


def term_score(text: str, term: str) -> int:
    term = normalize(term)
    if not term or term not in text:
        return 0
    return 3 if " " in term else 1


def reflect(event: str, limit: int = 3) -> dict:
    objects, config = load_data()
    clean = normalize(event)
    safety_hits = [term for term in config["safety_terms"] if normalize(term) in clean]
    excluded = set(config["safety_excluded_objects"] if safety_hits else [])

    ranked = []
    for object_id, profile in config["profiles"].items():
        if object_id in excluded:
            continue
        hits = [term for term in profile["terms"] if term_score(clean, term)]
        score = sum(term_score(clean, term) for term in hits)
        if score:
            ranked.append((score, len(hits), object_id, hits))
    ranked.sort(key=lambda row: (-row[0], -row[1], row[2]))

    selected = []
    for score, _, object_id, hits in ranked[:limit]:
        item = objects[object_id]
        selected.append(
            {
                "id": object_id,
                "title": item["title"],
                "status": item["status"],
                "evidence_level": item["evidence_level"],
                "matched_signals": hits,
                "selection_score": score,
                "knowledge": item["claim"],
                "does_not_establish": item["not_evidence_of"][0],
                "reflection_question": item["reflection_prompts"][0],
                "decision_boundary": item["decision_boundary"],
            }
        )

    return {
        "prototype": "asri-deterministic-v0.2",
        "event_echo": event.strip(),
        "safety": {
            "flagged": bool(safety_hits),
            "matched_terms": safety_hits,
            "message": (
                "A leírás közvetlen biztonsági vagy kényszerhelyzetet jelezhet. Az ASRI ebben a körben nem elemez kölcsönös felelősséget és nem sürget közös reflexiót."
                if safety_hits
                else None
            ),
        },
        "selected_objects": selected,
        "human_authorship": "A fenti elemek vizsgálati lehetőségek, nem ítéletek. Az értelmezést és a döntést te végzed.",
        "no_match": not selected,
    }


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Használat: python prototype/asri_reflection.py '<esemény>'")
    print(json.dumps(reflect(" ".join(sys.argv[1:])), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

