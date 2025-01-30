import streamlit as st
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path
import time
import pandas as pd
from PIL import Image
from io import BytesIO
import requests 

st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)

st.set_page_config(
  page_title="MIN-MAX-USING-GOLDEN-FIBO",
  page_icon="🔍",
  layout="wide",
  initial_sidebar_state="expanded",
) 

# --- Info ---

pg1 = st.Page(
    "pages/Theory.py",
    title="Theory",
    icon=":material/cognition:",
    default=True,
)

pg2 = st.Page(
    "pages/Fibo_Search.py",
    title="Fibo Search",
    icon=":material/search:"
)

pg3 = st.Page(
    "pages/Golden_Section_Search.py",
    title="Golden Section Search",
    icon=":material/search:"
)

pg = st.navigation(
    {
        "Info": [pg1],
        "Search Method": [pg2, pg3],
    }
)


pg.run()