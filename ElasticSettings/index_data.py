import pandas as pd
from numpy import float32
import logging
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

logging.basicConfig(level=logging.INFO)


def clean_data(metadata_path: str) -> pd.DataFrame:
    md = pd.read_csv(metadata_path)
    md_sorted = md.iloc[md.isnull().sum(1).sort_values(ascending=1).index]
    md_unique = md_sorted.drop_duplicates(subset=["cord_uid"], keep="first").copy()
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

    
def index_data(df: pd.DataFrame, index: str, es: Elasticsearch):
    bulk_data = []
    
    for idx, doc in df.iterrows():
        doc_dict = dict(doc)
        for key in doc_dict.keys():
            if pd.isna(doc_dict[key]):
                doc_dict[key] = None
    
        data = {
            "_index": index,
            "_id": idx,
            "_source": doc_dict
        }
        
        bulk_data.append(data)
    bulk(es, bulk_data)
    

