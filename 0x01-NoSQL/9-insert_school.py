#!/usr/bin/env python3
"""Inserts a document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a MongoDB collection

    Args:
        mongo_collection: the pymongo collection
        kwargs: the keyword arguments representing other fields

    Returns:
        returns the new ID of the inserted document
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
