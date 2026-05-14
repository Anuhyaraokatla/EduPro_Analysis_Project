import pandas as pd

def preprocess_data(users, courses, transactions):

    # ----------------------------
    # CLEAN COLUMN NAMES
    # ----------------------------
    users.columns = users.columns.astype(str).str.strip()
    courses.columns = courses.columns.astype(str).str.strip()
    transactions.columns = transactions.columns.astype(str).str.strip()

    # ----------------------------
    # STANDARDIZE COLUMN NAMES
    # ----------------------------
    rename_map_users = {
        "UserID": "user_id",
        "userID": "user_id"
    }

    rename_map_courses = {
        "CourseID": "course_id",
        "courseID": "course_id"
    }

    rename_map_transactions = {
        "UserID": "user_id",
        "CourseID": "course_id",
        "Amount": "amount",
        "TransactionID": "transaction_id"
    }

    users = users.rename(columns=rename_map_users)
    courses = courses.rename(columns=rename_map_courses)
    transactions = transactions.rename(columns=rename_map_transactions)

    # ----------------------------
    # VALIDATION (IMPORTANT)
    # ----------------------------
    required_cols = ["user_id", "course_id"]

    for col in required_cols:
        if col not in transactions.columns:
            raise KeyError(f"{col} not found in transactions: {transactions.columns.tolist()}")

    # ----------------------------
    # MERGING DATASETS
    # ----------------------------
    merged = transactions.merge(users, on="user_id", how="left")
    merged = merged.merge(courses, on="course_id", how="left")

    return merged