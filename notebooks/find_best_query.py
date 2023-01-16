from ElasticSettings.analyze_settings import settings
from ElasticSettings.mappings import mappings
from ElasticSettings.index_data import index_data, clean_data
from ElasticSettings.topics import create_run, create_eval
from elasticsearch import Elasticsearch
from credentials import username, password
from functools import partial
import numpy as np
from dataclasses import dataclass
from typing import Union
import json

@dataclass
class test_range:
    field_name: str
    start_val: Union[int, float]
    end_val: Union[int, float]
    step: Union[int, float]


def query_tuner(param_to_tune: str):
    es = Elasticsearch("http://localhost:9200",
        basic_auth=(username, password))

    previous_tuner_value = None
    previous_settings = None
    current_settings = None
    eval_history = []

    ranges = [
        test_range("title", 1, 3.6, 0.2),
        test_range("abstract", 1, 3.6, 0.2)
    ]

    for rng in ranges:
        for val in np.arange(rng.start_val, rng.end_val, rng.step):

            function_params = {}

            # fill ranges that are not used
            

            function_params[rng.field_name] = val
            function_params["origin"] = "2020-05-15"
            function_params["scale"] = "4m"
            function_params["offset"] = "1m"
            function_params["decay"] = 0.5
            function_params["decay_function_type"] = "exp"

            eval = run_test(es, function_params=function_params)
            eval_history.append(eval)
            current_tuner_value = eval[param_to_tune]

            if previous_tuner_value:
                if current_tuner_value < previous_tuner_value:
                    # newer value is better continue search
                    print("value got better")
                    pass
                else:
                    print("previous settings were better")
                    break        
            
            previous_settings = function_params
            previous_tuner_value = current_tuner_value
                



def run_test(es, function_params):
    index_name = "test_index"
        
    topics_path = "data/topics-rnd5_covid-complete.xml"
    qrels_path = "data/qrels-covid_d5_j0.5-5_covid-complete.txt"

    runs_folder = "runs/query_tests/"

    run_name = create_run(topics_path=topics_path, es=es, index=index_name, runs_folder=runs_folder, query_func=partial(query_func, function_params=function_params))
    run_path = runs_folder + run_name
    eval = create_eval(qrels_path, run_path=run_path)

    return eval


def query_func(function_params: dict, q):
    query = {
        "query": { 
            "function_score": {
                    "query": {
                        "multi_match": {
                            "query": q,
                            "type": "cross_fields",
                            "fields": [
                                "source_x",
                                f"title^{function_params['title']}",
                                f"abstract^{function_params['abstract']}",
                                "journal",
                                "authors"
                                ]}
                            },
                    function_params["decay_function_type"]: {
                        "publish_time": {
                            "origin": function_params["origin"],
                            "scale": function_params["scale"],
                            "offset": function_params["offset"],
                            "decay": function_params["decay"]
                        }
                    }
                  }       
        }
    }

    return query




if __name__ == '__main__':
    query_tuner("map")