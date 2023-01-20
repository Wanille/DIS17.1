settings = {
    "analysis": {
        "analyzer": {
            "my-analyzer": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "stop",
                    "synonym",
                    "snowballer"
                ]
            }
        },
        "filter": {
            "snowballer": {
                "type": "snowball",
                "language": "English"
            },
            "synonym": {
                "type": "synonym",
                "synonyms_path": "synonyms.txt"
            }
        }
    },
    "similarity": {
        "my-similarity": {
            "type": "BM25",
            "k1": 0.9,
            "b": 0.6
        }
    }
}
