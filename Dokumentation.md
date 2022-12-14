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
