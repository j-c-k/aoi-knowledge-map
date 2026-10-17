# Adaptive Self-Reflection Infrastructure (ASRI)

Az **Adaptive Self-Reflection Infrastructure** nyílt, verziózott tudásmagja. A projekt célja, hogy az emberi működésről már rendelkezésre álló ismereteket valós élethelyzetekhez kapcsolható, személyre szabható önreflexiós tanulási egységekké alakítsa.

Az ASRI nem terápia, nem diagnosztikai rendszer, nem ideológia és nem döntéshozó. Az ember végzi az önreflexiós munkát, az ember választ, és ő viseli a választás következményeit. Az AI szerepe: **tanár + tükör + memória + következetesség-ellenőrző**.

## Jelenlegi állapot: v0.2 baseline

- `CONSTITUTION.md` — nem feladható tervezési elvek;
- `taxonomy/knowledge-map-v0.1.md` — a tudástérkép első taxonómiája;
- `schema/knowledge-object.schema.json` — géppel ellenőrizhető Knowledge Object séma;
- `knowledge_objects/core-v0.1.yaml` — 32 forrásolt Knowledge Object: 26 stable, 6 draft;
- `sources/source-registry.yaml` — 58 tételes, DOI/URL-alapú forrásjegyzék;
- `protocols/reflection-loop-v0.1.md` — a reflexiós ciklus;
- `governance/evidence-and-status.md` — evidencia- és státuszszabályok;
- `prototype/` — futtatható determinisztikus relevancia- és reflexiós baseline;
- `tests/` — valós élethelyzet-alapú regressziós és biztonsági próbák;
- `AUDIT.md` — auditjelentés és nyitott kérdések.

## Gyors próba

```bash
python prototype/asri_reflection.py "Napok óta újra és újra gondolok rá, de nem jutok tovább."
python -m unittest discover -s tests -v
```

A baseline nem értelmező AI: mérhető minimum arra, hogy a későbbi modellekhez képest tudjuk, javult-e a relevanciaválasztás anélkül, hogy nőtt volna a diagnosztizálás, tanácsadás vagy hamis bizonyosság.

## Nyelv

A kanonikus nemzetközi név **Adaptive Self-Reflection Infrastructure (ASRI)**. A fejlesztési dokumentáció jelenleg magyar, a gépi mezőnevek és a nemzetközi-facing fogalmak angolok.

## Fontos korlát

A Knowledge Objectek oktatási és önreflexiós eszközök. Nem használhatók klinikai diagnózis, kockázatbecslés, alkalmassági döntés, jogi minősítés vagy egy személy „valódi” személyiségének automatikus meghatározására.
