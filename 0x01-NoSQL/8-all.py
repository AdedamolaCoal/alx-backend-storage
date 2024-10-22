#!/usr/bin/env python3
"""returns a list of all documents in a collection"""


def list_all(mongo_collection):
    """Lists all documents in a Mongo Collection

    Args:
        mongo_collection : the Mongo Collection

    Returns:
        list of documents or empty list if no documents found
    """
    return list(mongo_collection.find({})) or []
