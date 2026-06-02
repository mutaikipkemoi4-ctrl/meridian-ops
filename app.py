import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Meridian Ops", layout="wide")

with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder"]
    choice = st.radio("Navigation", menu)

st.title(f"Meridian Ops: {choice}")

if choice == "Data Sanitizer":
    uploaded_file = st.file_uploader("Upload your data", type=["csv", "xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.session_state['data'] = df
        st.success("Data uploaded successfully!")
        st.dataframe(df.head())

elif choice == "Dashboard Builder":
    if 'data' in st.session_state:
        df = st.session_state['data']
        x_axis = st.selectbox("X-Axis", df.columns)
        y_axis = st.selectbox("Y-Axis", df.columns)
        fig = px.bar(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)
        
        st.markdown("### Strategic Briefing")
        st.write("1. **What:** Performance analysis of " + y_axis)
        st.write("2. **Why:** Indicates current efficiency trends.")
    else:
        st.warning("Please upload a file in Data Sanitizer first.")
