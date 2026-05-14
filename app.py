import sys
import os
import pandas as pd
import streamlit as st

# ----------------------------
# FIX: allow src import
# ----------------------------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing import preprocess_data

st.set_page_config(page_title="EduPro Dashboard", layout="wide")
st.title("📊 EduPro Online Platform Dashboard")

# ----------------------------
# DOWNLOADS PATH
# ----------------------------
DATA_DIR = r"C:\Users\MYPC\Downloads"


# ----------------------------
# AUTO FIND FILE FUNCTION
# ----------------------------
def find_file(name):
    """
    Tries multiple variations:
    Users, Users.csv, Users.csv.csv
    """
    possible_names = [
        name,
        f"{name}.csv",
        f"{name}.csv.csv"
    ]

    for file in possible_names:
        path = os.path.join(DATA_DIR, file)
        if os.path.exists(path):
            return path

    return None


# ----------------------------
# SAFE CSV LOADER
# ----------------------------
def load_csv(name):
    path = find_file(name)

    if path is None:
        st.error(f"❌ File not found: {name}")
        return None

    try:
        df = pd.read_csv(path, encoding="utf-8-sig", engine="python")

        if df.shape[1] == 1:
            df = pd.read_csv(path, encoding="utf-8-sig", sep=None, engine="python")

        df.columns = df.columns.astype(str).str.strip()
        return df

    except Exception as e:
        st.error(f"Error loading {path}: {e}")
        return None


# ----------------------------
# LOAD DATA (AUTO DETECTS FILES)
# ----------------------------
users = load_csv("Users")
courses = load_csv("Courses")
transactions = load_csv("Transactions")


# STOP IF ANY FAIL
if users is None or courses is None or transactions is None:
    st.stop()


# ----------------------------
# DEBUG
# ----------------------------
st.subheader("🔍 Columns Check")

st.write("Users:", users.columns.tolist())
st.write("Courses:", courses.columns.tolist())
st.write("Transactions:", transactions.columns.tolist())


# ----------------------------
# RAW DATA
# ----------------------------
st.subheader("📂 Raw Data")

st.dataframe(users.head())
st.dataframe(courses.head())
st.dataframe(transactions.head())


# ----------------------------
# PREPROCESS
# ----------------------------
try:
    df = preprocess_data(users, courses, transactions)
except Exception as e:
    st.error(f"Preprocessing failed: {e}")
    st.stop()

st.success("✅ Data loaded successfully!")


# ----------------------------
# KPI METRICS
# ----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Users", df["user_id"].nunique())

with col2:
    st.metric("Total Courses", df["course_id"].nunique())

with col3:
    if "amount" in df.columns:
        st.metric("Total Revenue", df["amount"].sum())


# ----------------------------
# CHARTS
# ----------------------------
st.subheader("📈 Top Courses")

st.bar_chart(df["course_id"].value_counts().head(10))

st.subheader("👤 Top Users")

st.bar_chart(df["user_id"].value_counts().head(10))