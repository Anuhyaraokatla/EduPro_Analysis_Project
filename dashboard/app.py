import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_loader import load_csv
from src.preprocessing import preprocess_data
from src.analysis import generate_kpis

import streamlit as st