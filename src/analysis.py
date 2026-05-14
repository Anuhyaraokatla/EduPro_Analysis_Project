def generate_insights(df):

    insights = {}

    # ----------------------------
    # BASIC METRICS
    # ----------------------------
    insights["total_users"] = df["user_id"].nunique() if "user_id" in df else 0
    insights["total_courses"] = df["course_id"].nunique() if "course_id" in df else 0
    insights["total_transactions"] = len(df)

    # ----------------------------
    # REVENUE
    # ----------------------------
    if "amount" in df.columns:
        insights["total_revenue"] = float(df["amount"].sum())
        insights["average_transaction"] = float(df["amount"].mean())

    # ----------------------------
    # TOPS
    # ----------------------------
    if "course_id" in df.columns:
        insights["top_courses"] = df["course_id"].value_counts().head(5).to_dict()

    if "user_id" in df.columns:
        insights["top_users"] = df["user_id"].value_counts().head(5).to_dict()

    return insights