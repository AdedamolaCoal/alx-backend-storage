#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in Mongo"""

from pymongo import MongoClient


def log_stats():
    """Gives the Nginx log stats for the collection nginx

    Args:
    - None

    Returns:
    - None
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count_method = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count_method}")

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
