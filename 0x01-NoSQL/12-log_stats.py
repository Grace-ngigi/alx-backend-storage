#!/usr/bin/env python3
''' script that provides some stats about nginx stored in mongoDB '''
import pymongo


def nginx_stats(mongo_collection):
    ''' get nginx stats '''
    total count = mongo_collection.count_document({})
    print(f"Total logs: {total_logs}")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\t{method}: {count}")

    specific_log_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"Number of logs with method=GET and path=/status: {specific_log_count}")


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]
    nginx_stats(collection)
