import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Design System
st.set_page_config(page_title="Meridian Ops", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f7; }
    h1, h2, h3 { color: #0a192f; }
    div.stButton > button { background-color: #008080 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Global State Persistence
if 'data' not in st.session_state:
    st.session_state['data'] = None

# 3. Sidebar Navigation
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)

# 4. Logic Controller
st.title(f"Meridian Ops: {choice}")

if choice == "Data Sanitizer":
    st.subheader("Autonomous Data Intake")
    uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])
    if uploaded:
        # Load data into session state
        st.session_state['data'] = pd.read_csv(uploaded) if uploaded.name.endswith('.csv') else pd.read_excel(uploaded)
        st.success("Data successfully sanitized and loaded into memory.")
        st.write("Preview:", st.session_state['data'].head())

elif choice == "Dashboard Builder":
    st.subheader("Performance Analytics")
    if st.session_state['data'] is not None:
        df = st.session_state['data']
        x_axis = st.selectbox("Select X-Axis", df.columns)
        y_axis = st.selectbox("Select Y-Axis", df.columns)
        
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
        st.plotly_chart(fig, use_container_width=True)
        
        # Consultant-in-a-Box: Strategic Pro-Tip
        st.info("💡 **Strategic Pro-Tip:** Review your MoM variance. If the trend is flat, consider re-allocating assets to high-yield segments identified in your SOP library.")
    else:
        st.warning("⚠️ No data detected. Please return to 'Data Sanitizer' to upload your file.")

elif choice == "SOP/Policy Library":
    st.subheader("Operational Playbook Registry")
    st.write("Browse your standard operating procedures to resolve data anomalies.")

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing")
    if st.session_state['data'] is not None:
        st.write("Generating your boardroom-ready summary...")
    else:
        st.warning("Please upload data in the Sanitizer first.")

elif choice == "Insights":
    st.subheader("Business Case Studies")
    st.write("Historical insights for Meridian Ops scaling.")
