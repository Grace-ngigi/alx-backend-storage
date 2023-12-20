#!/usr/bin/env python3
''' update doc '''
import pymongo


def update_topics(mongo_collection, name, topics):
    ''' change school topics '''
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
