def get_query(q: str):
    query = {
        "query": {
            "multi_match": {
                    "query": {q},
                    "type": "cross_fields",
                    "fields": [
                        "source_x",
                        "title^3",
                        "abstract^2",
                        "journal",
                        "authors"
                ]}
        }
    }