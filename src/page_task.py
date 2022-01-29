import streamlit as st
import bokeh
import bokeh.models
import bokeh.plotting
import numpy as np
import pandas as pd
import sklearn
import billboard

from sentence_transformers import SentenceTransformer

def task():
    model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    model = SentenceTransformer(model_name)
    chart = billboard.ChartData("hot-100")
    print(chart)
    st.write("test")
