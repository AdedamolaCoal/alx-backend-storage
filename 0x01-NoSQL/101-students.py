#!/usr/bin/env python3
"""returns all students sorted by average score"""

# from pymongo import MongoClient


# def top_students(mongo_collection):
#     """returns all students sorted by average score

#     Args:
#       - mongo_collection: the pymongo collection

#     Returns:
#       - list of students sorted by average score
#     """
#     return mongo_collection.find().sort([("averageScore", -1)])


def top_students(mongo_collection):
    """Returns all students sorted by average score

    Use the MongoDB aggregation framework to:
    Unwind the topics array to calculate individual scores.
    Calculate the average score for each student.
    Sort the students by their average score in descending order.
    """
    pipeline = [
        {"$project": {"name": 1, "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}},
    ]

    return list(mongo_collection.aggregate(pipeline))
