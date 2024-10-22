#!/usr/bin/env python3
"""Returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic

    Args:
        - mongo_collection: the pymongo collection
        - topic: the topic of the school
    """
    res = mongo_collection.find({"topics": topic})
    return list(res)
