import streamlit as st
import pandas as pd
import plotly.express as px
import openai

# Everything else goes below these imports...
st.set_page_config(page_title="Meridian Ops", layout="wide")

# Now 'st' is defined and safe to use
with st.sidebar:
    st.title("Meridian Ops")
    # ... rest of your code
