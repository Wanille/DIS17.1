mappings = {
    "properties": {
        "cord_uid": {"type": "keyword"},
        "sha": {"type": "keyword"},
        "source_x": {"type": "keyword"},
        "title":{"type": "text", "analyzer": "my-analyzer"},
        "doi": {"type": "keyword"},
        "pmcid": {"type": "keyword"},
        "pubmed_id": {"type": "integer"},
        "license": {"type": "keyword"},
        "abstract": {"type": "text", "analyzer":"my-analyzer"},
        "publish_time": {"type": "date"},
        "authors": {"type": "text"},
        "journal": {"type": "text"},
        "mag_id": {"type": "keyword"},
        "who_covidence_id": {"type": "keyword"},
        "arxiv_id": {"type": "keyword"},
        "pdf_json_files": {"type": "keyword"},
        "pmc_json_files": {"type": "keyword"},
        "url": {"type": "keyword"},
        "s2_id": {"type": "keyword"}
    }
}