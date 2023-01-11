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
                    "gauss": {
                        "publish_time": {
                            "origin": "2021-12-31",
                            "scale": "20m",
                            "offset": "3m",
                            "decay": 0.3
                        }
                    }
                  },
            
                
        }
    }
    return query