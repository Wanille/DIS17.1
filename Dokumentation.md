Aufgaben:

- Analyzing Documents
     - character filtering, tokenization, token filtering
     - clean the data, e.g., separate list elements
     - Enrichment via further data (full text, embeddings)
     - etc.
- Indexing the Data
     - Define Mapping strategies for fields à Elastic
- Query Analysis
     - Analyze queries
     - Match-Types and compound queries
     - Boosting specific matches
     - Additive vs. multiplicative boosting
     - Expand queries with further information


## Indexing Data
Es kann nur eins von beiden verwendet werden: Entweder Noramlizer oder Analyzer.
Wir überprüfen, Number ret, Number rel, Number rel rev, Pressicion, Pressicion at 5 (10,15,20,25)

### Session 2022-12-07

- Entscheidung ob analyzer oder normalizer benutzt wird --> ANALYZER (wegen Volltextsuche)
- analyzer für indexingpipeling und query 
- synonymfilter (teil des tokenfilters) für COVID19 wörter aller art --> SUPI
- synonymfilter getestet -> klappt
- Analyzer eingefügt
- Mapping fertig gestellt


### Session 2022-12-14

- tokenfilter (analyzer): "lowercase", "stop", "classic", "snowballer", "synonym", "asciifolding"
    
synonyme : 
- SARS-CoV-2
- COVID-19
- coronavirus
- SARS-CoV2
- SARS-CoV
- COVID
- covid 19
- covid- 19
- covid-19

- COVID19 synonymfilter eingebaut
- Ältere Dokumente nach hinten schieben Query (boosting)

### Session 2023-01-04

Überlegungen zu Query analysis, weil piepline nicht funktioniert hat (nils wir brauchen dich)

#### Boosting 
wir benutzen: multiplicative boosting => function query 

- weight von multi match erhöhen 
- nur ein feld boosten mit ^ ( welche felder brauchen wir ?)
- type von query verändern z.b. best_fields

- anfrage instanz an elasticsearch verändern, z.b. auch question 
- query field, source_x, author und journal macht wenig sinn bei den queries

### Session 2023-01-11
Wir haben hinuugefügt:

- Negatives Boosting von älteren Dokumenten, mit einer Scale von 20 Monaten und einem Cutoff von 3 Monaten
- Wir erhoffen uns dadurch ein besseres Suchergebniss durch relevantere/modernere Dokumente

- Änderungen an der Index Pipeline:
     - Neu Indexierung kann nun "geskipped" werden, nur Anfrage wird gestellt
     - Ausgabedatei nun nicht mehr .txt sondern .json, dadurch bessere importmöglichkeiten für evtl. visualisierung 
 
 ### Session 2023-01-13
 
 Wir hatten eine extrem schlechte P5 (0.29) und num_rel_ret 608 ( Baseline im Vergleich ~9000)
 Wir haben unsere query zurück auf Werkseinstellung gesetzt und ein besseres Ergebnis erhalten P5 0.468 und num_rel_ret 9965
 
 Plan: Herausfinden was bei Query analysis schief geht.
 
 ### Session 2023-01-16
 
 query-parameter tuning --> beste Parameter-einstellung finden 
 automatisches tuning doch zu aufwändig
 - wenn publish-time function-score eingefügt wird, verschlechtert sich der MAP-wert enorm auf 0.0035 (ohne 0.19)
 - synonym filter hat map-wert auf 0.2029 gebracht(Verbesserung um 0.0007) num_rel_ret ist auf 10276 (148) gestiegen 
 
