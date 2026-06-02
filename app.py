import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Meridian Ops", layout="wide")

# 2. Sidebar with Persistent Navigation
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)
    st.write("---")
    st.markdown("### Professional Tools")
    st.link_button("Book Strategy Session", "https://calendly.com/your-calendar-link")

# 3. Enhanced Module Logic
st.title(f"Meridian Ops: {choice}")

if choice == "Data Sanitizer":
    st.subheader("Professional Data Intake")
    uploaded_file = st.file_uploader("Upload your data (CSV/Excel)", type=["csv", "xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.success("Data ingested successfully.")
        st.session_state['data'] = df
        st.dataframe(df.head())

elif choice == "Dashboard Builder":
    if 'data' in st.session_state:
        st.write("Select columns to visualize:")
        cols = st.session_state['data'].columns.tolist()
        x_axis = st.selectbox("X-Axis", cols)
        y_axis = st.selectbox("Y-Axis", cols)
        fig = px.bar(st.session_state['data'], x=x_axis, y=y_axis, title="Strategic Insights")
        st.plotly_chart(fig)
    else:
        st.warning("Please upload a file in the 'Data Sanitizer' module first.")

elif choice == "SOP/Policy Library":
    st.subheader("Technical Operations & Policy Manuals")
    category = st.selectbox("Select Category", ["Agribusiness", "Tea Industry", "Operational Strategy", "Sports/Performance"])
    
    docs = {
        "Agribusiness": {"Black Soldier Fly Bio-Refinery": "Details on larval production and bio-refining."},
        "Tea Industry": {"Understanding Kenyan Tea Grades": "Manual on BP1, PF1, and auction standards."},
        "Operational Strategy": {"Meridian Ops Methodology": "Strategic framework for performance scaling."},
        "Sports/Performance": {"The HYROX Protocol": "Comprehensive guide for tactical fitness pacing."}
    }
    
    if category in docs:
        selected_doc = st.selectbox("Select Manual", list(docs[category].keys()))
        st.info(f"**{selected_doc}**")
        st.write(docs[category][selected_doc])
        st.button("Download PDF/Full Report")
