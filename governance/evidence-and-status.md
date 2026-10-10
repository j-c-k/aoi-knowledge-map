# Evidence and release status

Az `evidence_level` és a `status` két külön dimenzió.

## Evidenciaszint

- **A — convergent synthesis:** több jó minőségű meta-analízis/szisztematikus áttekintés vagy széles szakmai konszenzus támogatja a szűken megfogalmazott állítást.
- **B — established but bounded:** több módszerből származó, reprodukált empirikus eredmény vagy erős szakmai áttekintés; fontos határokkal.
- **C — mixed/emerging:** értelmes és kutatható konstrukció, de heterogén definíciók, vegyes eredmények vagy korlátozott általánosíthatóság.
- **D — conceptual/source hypothesis:** filozófiai, klinikai vagy gyakorlati hipotézis; nem kezelhető empirikus tényként.

Az evidenciaszint mindig az objektum `claim` mezőjének szűk állítására vonatkozik, nem a teljes témára.

## Kiadási státusz

- **draft:** használható kutatási prototípusban, de definíciója, forrásai, határai vagy ASRI-alkalmazása további auditot igényel.
- **stable:** legalább két releváns forrás; pontos definíció; explicit `not_evidence_of`; nem diagnosztikus használat; emberi döntési szuverenitást őrző prompt; belső sémaellenőrzés teljesült.
- **deprecated:** megtartott történeti elem, amelyet jobb vagy pontosabb objektum váltott fel.

## Forráshierarchia

1. szisztematikus review/meta-analízis és nagy szakmai áttekintés;
2. több, egymástól független elsődleges vizsgálat;
3. klasszikus elméleti/filozófiai elsődleges szöveg;
4. gyakorlati vagy self-help forrás — kizárólag hipotézisgenerálásra.

## Stable nem jelent véglegest

A `stable` azt jelenti, hogy az objektum jelen verziója publikálható a fenti korlátokkal. Új evidenciára minden elem visszaminősíthető vagy módosítható.

