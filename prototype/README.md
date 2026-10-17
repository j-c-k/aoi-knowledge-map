# ASRI deterministic prototype v0.2

Ez az első futtatható **relevance-engine baseline**. Nem chatbot és nem „saját AI”. Azt teszteli, hogy egy rövid, magyar nyelvű valós élethelyzetből kiválasztható-e legfeljebb három releváns Knowledge Object úgy, hogy közben ne diagnosztizáljon és ne adjon döntést.

## Futtatás

```bash
python prototype/asri_reflection.py "Megint azt mondtam, hogy nem érdekel, pedig nagyon is érdekelt."
python -m unittest discover -s tests -v
```

## Kimenet

- a bemenet tényszerű visszaidézése;
- 1–3 releváns Knowledge Object és a kiválasztás oka;
- minden objektumhoz egy `not_evidence_of` korlát;
- egyetlen önreflexiós kérdés;
- explicit döntési szuverenitás;
- biztonsági jelzés, ha erőszak, kényszer vagy közvetlen veszély nyelve jelenik meg.

## Mit nem bizonyít?

A kulcsszavas baseline nem értelmezi megbízhatóan az iróniát, tagadást, összetett kontextust vagy rejtett jelentést. Célja a későbbi LLM-alapú relevanciamotor mérési minimumának és kimeneti szerződésének rögzítése.

