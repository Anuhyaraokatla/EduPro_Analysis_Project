import pandas as pd
import os

# ----------------------------
# PROJECT DATA FOLDER
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")


# ----------------------------
# LOAD CSV
# ----------------------------
def load_csv(filename):

    path = os.path.join(DATA_DIR, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {filename}")

    df = pd.read_csv(path, encoding="utf-8-sig")

    # clean column names
    df.columns = df.columns.astype(str).str.strip()

    return df