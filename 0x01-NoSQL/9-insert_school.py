#!/usr/bin/env python3
''' insert doc '''
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    ''' insert doc '''
    new_doc = mongo_collection.insert_one(kwargs)
    return inserted_id
