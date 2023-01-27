import pandas as pd
from numpy import float32
import logging
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from elasticsearch.helpers import bulk
import json

logging.basicConfig(level=logging.INFO)


def clean_data(metadata_path: str) -> pd.DataFrame:
    md = pd.read_csv(metadata_path)
    md_sorted = md.iloc[md.isnull().sum(1).sort_values(ascending=1).index]
    md_unique = md_sorted.drop_duplicates(subset=["cord_uid"], keep="first").copy()
    # md_unique["abstract_processed"] = md_unique["abstract"].apply(synonyms_replacer)
    # md_unique["title_processed"] = md_unique["title"].apply(synonyms_replacer)
    md_unique.reset_index(inplace=True, drop=True)

    for col in ["pubmed_id", "arxiv_id"]:
        md_unique[col] = md_unique[col].apply(check_float)
        # md_unique[col] = md_unique[col].astype(float)
    return md_unique


def check_float(value) -> bool:
    try:
        convert_float = float(value)
        return convert_float
    except ValueError:
        return pd.NA

    
def index_data(df: pd.DataFrame, index: str, es: Elasticsearch, keywords = None):
    bulk_data = []

    if keywords:
        keywords_ls = json.load(open(keywords, "r"))
    
    for idx, doc in df.iterrows():
        doc_dict = dict(doc)

        for key in doc_dict.keys():
            if pd.isna(doc_dict[key]):
                doc_dict[key] = None


        if keywords:
            keywords_in_text = []
            text_complete = ""
            if type(doc_dict["abstract"]) == str:
                text_complete += doc_dict["abstract"]
            if type(doc_dict["title"]) == str:
                text_complete += doc_dict["title"]

            for keyword in keywords_ls:
                if keyword in text_complete:
                    keywords_in_text.append(keyword)

            doc_dict["keywords"] = " ".join(keywords_in_text)

        data = {
            "_index": index,
            "_id": idx,
            "_source": doc_dict
        }
        
        bulk_data.append(data)
    bulk(es, bulk_data)
    

