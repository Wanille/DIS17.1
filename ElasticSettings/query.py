def get_query(q: str):
    query = {
        "query": {
            "function_score": {
                "query": { 
                    "multi_match": {
                        "query": q,
                        "type": "cross_fields",
                        "fields": [
                            "title",
                            "abstract"
                            ]}},  
                "exp": {
                    "publish_time": {
                        "origin": "2020-05",
                        "scale": "100d",
                        "decay": 0.9
                    }
                }
            }}
    }
    return query