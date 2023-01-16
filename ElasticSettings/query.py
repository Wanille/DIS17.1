def get_query(q: str):
    query = {
        "query": { 
            "function_score": {
                    "query": {
                        "multi_match": {
                            "query": q,
                            "type": "cross_fields",
                            "fields": [
                                "source_x",
                                "title^3",
                                "abstract^2",
                                "journal",
                                "authors"
                                ]}},
                    "exp": {
                        "publish_time": {
                            "origin": "2020-05-15",
                            "scale": "4m",
                            "offset": "1m",
                            "decay": 0.5
                        }
                    }
                  }       
        }
    }

    return query