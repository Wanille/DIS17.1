import pandas as pd
from elasticsearch import Elasticsearch
from ElasticSettings.query import get_query
from datetime import datetime
import pytrec_eval
import json


def create_run(topics_path: str, es: Elasticsearch, index: str, runs_folder: str) -> str:
    
    topics = load_topics(topics_path=topics_path)
    run_name = datetime.strftime(datetime.now(), "%y.%m.%d_%H:%M") + ".txt"

    with open(f"{runs_folder}{run_name}", "w") as fp:
        for idx, doc in topics.iterrows():
            hits = search(doc["query"], es, index)
            
            for rank, hit in enumerate(hits):
                line = " ".join([str(idx), str(0), hit["_source"]["cord_uid"], str(rank), str(hit["_score"]), run_name, "\n"])
                fp.write(line)
    return run_name
 

def create_eval(qrels_path, run_path) -> dict:
    with open(qrels_path, 'r') as f_qrel:
        qrel = pytrec_eval.parse_qrel(f_qrel)
    with open(run_path, 'r') as f_run:
        run = pytrec_eval.parse_run(f_run)

    evaluator = pytrec_eval.RelevanceEvaluator(qrel, pytrec_eval.supported_measures)
    results = evaluator.evaluate(run)

    mesure_agg_dict = {}
    measures = list(results[list(results.keys())[0]].keys())
    for measure in sorted(measures):
            mesure_agg_dict[measure] = pytrec_eval.compute_aggregated_measure(measure, [query_measures[measure] for query_measures in results.values()])
    return mesure_agg_dict


def load_topics(topics_path: str) -> pd.DataFrame:
    topics = pd.read_xml(topics_path)
    topics.set_index("number", inplace=True)
    return topics


def search(q: str, es: Elasticsearch, index: str) -> list:
    q = get_query(q=q)
    result = es.search(index=index, body=q, size=1000)
    hits = result["hits"]["hits"]
    return hits