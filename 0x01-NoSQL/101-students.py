#!/usr/bin/env python3
"""returns all students sorted by average score"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students sorted by average score

    Args:
      - mongo_collection: the pymongo collection

    Returns:
      - list of students sorted by average score
    """
    return mongo_collection.find().sort([("averageScore", -1)])
