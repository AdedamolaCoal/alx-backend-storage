#!/usr/bin/env python3
"""Updates the topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school document based on the name

    Args:
    - mongo_collection: the pymongo collection
    - name: the name of the school
    - topics: the list of topics of the school

    Returns:
    - None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
