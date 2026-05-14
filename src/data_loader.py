import pandas as pd
import os

# ----------------------------
# DOWNLOADS PATH (YOUR SETUP)
# ----------------------------
DATA_DIR = r"C:\Users\MYPC\Downloads"


# ----------------------------
# FIND FILE AUTOMATICALLY
# ----------------------------
def find_file(name):
    """
    Tries multiple formats:
    Users
    Users.csv
    Users.csv.csv
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
        raise FileNotFoundError(
            f"❌ File '{name}' not found in Downloads folder."
        )

    try:
        df = pd.read_csv(path, encoding="utf-8-sig", engine="python")

        # fallback if bad formatting
        if df.shape[1] == 1:
            df = pd.read_csv(path, encoding="utf-8-sig", sep=None, engine="python")

        # clean column names
        df.columns = df.columns.astype(str).str.strip()

        return df

    except Exception as e:
        raise Exception(f"Error loading {path}: {e}")