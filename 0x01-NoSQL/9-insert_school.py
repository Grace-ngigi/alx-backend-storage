#!/usr/bin/env python3
''' insert doc '''
import pymongo


def insert_school(mongo_collection, **kwargs):
    ''' insert doc '''
    return mongo_collection.insert_one(kwargs).inserted_id
