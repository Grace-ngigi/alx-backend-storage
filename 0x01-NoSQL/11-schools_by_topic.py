#!/usr/bin/env python3
''' find doc '''
import pymongo


def schools_by_topic(mongo_collection, topic):
    ''' find doc '''
    return mongo_collection.find({"topics": topic})
