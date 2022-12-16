from ElasticSettings.analyze_settings import settings
from ElasticSettings.mappings import mappings
from ElasticSettings.index_data import index_data, clean_data
from ElasticSettings.topics import create_run, create_eval
from elasticsearch import Elasticsearch
from credentials import username, password
import json


def main():
    es = Elasticsearch("http://localhost:9200",
                   basic_auth=(username, password))

    data = clean_data("data/metadata.csv")

    index_name = "test_index"

    try:
        es.indices.delete(index=index_name)
    except:
        pass

    es.indices.create(index=index_name, mappings=mappings, settings=settings)

    index_data(df=data, index="test_index", es=es)

    topics_path = "data/topics-rnd5_covid-complete.xml"
    qrels_path = "data/qrels-covid_d5_j0.5-5_covid-complete.txt"

    run_path = create_run(topics_path=topics_path, es=es, index="test_index")
    eval = create_eval(qrels_path, run_path=f"data/runs/{run_path}")

    with open(f"data/runs/{run_path}.info", "w") as fp:
        fp.write(f"Info file for run: {run_path}\n\n")
        fp.write(f"Settings: ")
        fp.write(json.dumps(settings, indent=1))
        fp.write("\n\n")
        fp.write(f"Mappings: ")
        fp.write(json.dumps(mappings, indent=1))
        fp.write("\n\n")
        fp.write(f"Evaluation: ")
        fp.write(json.dumps(eval, indent=1))


if __name__ == '__main__':
    main()