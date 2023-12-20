#!/usr/bin/env python3
''' find and sort '''
import pymongo


def top_students(mongo_collection):
    ''' use aggregation to sort collection '''
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
