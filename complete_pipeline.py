from ElasticSettings.analyze_settings import settings
from ElasticSettings.mappings import mappings
from ElasticSettings.index_data import index_data, clean_data
from ElasticSettings.topics import create_run, create_eval
from ElasticSettings.query import get_query
from elasticsearch import Elasticsearch
from credentials import username, password
import json

from pprint import pprint

import logging


def main(skip_index: bool = False):
    es = Elasticsearch("http://localhost:9200",
            basic_auth=(username, password),
            request_timeout=60,
            retry_on_timeout=True,
            max_retries=10)

    index_name = "test_index"

    if not skip_index:
        data = clean_data("data/metadata.csv")

        try:
            es.indices.delete(index=index_name)
        except:
            pass

        es.indices.create(index=index_name, mappings=mappings, settings=settings)
        index_data(df=data, index=index_name, es=es)
        

    topics_path = "data/topics-rnd5_covid-complete.xml"
    qrels_path = "data/qrels-covid_d5_j0.5-5_covid-complete.txt"

    runs_folder = "runs/"

    run_name = create_run(topics_path=topics_path, es=es, index=index_name, runs_folder=runs_folder)
    run_path = runs_folder + run_name
    eval = create_eval(qrels_path, run_path=run_path)

    run_dict = {}

    run_dict["info"] = run_name
    run_dict["settings"] = settings
    run_dict["mappings"] = mappings
    run_dict["query"] = get_query(q="<sample_query>")
    run_dict["evaluation"] = eval
    

    json.dump(run_dict, open(f"{run_path}.info", "w"), indent=1)

    print("map", run_dict["evaluation"]["map"])
    print("P5", run_dict["evaluation"]["P_5"])
    print("P10", run_dict["evaluation"]["P_10"])
    print("P100", run_dict["evaluation"]["P_100"])
    print("num_rel_ret", run_dict["evaluation"]["num_rel_ret"])
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main(skip_index=False)  