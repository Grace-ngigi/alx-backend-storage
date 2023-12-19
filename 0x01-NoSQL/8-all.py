#!/usr/bin/env python3
''' list all docs '''
import pymongo


def list_all(mongo_collection):
    ''' List all docs '''
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
