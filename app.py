import streamlit as st
import pandas as pd
import plotly.express as px
import openai

# 1. Page Configuration
st.set_page_config(page_title="Meridian Ops", layout="wide", page_icon="📈")

# 2. Executive Design System
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f7; color: #0a192f; }
    [data-testid="stSidebar"] { background-color: #0a192f; color: white; }
    h1, h2, h3 { color: #0a192f !important; font-family: 'Segoe UI', sans-serif; }
    div.stButton > button { background-color: #008080 !important; color: white !important; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# 3. State Initialization
if 'data' not in st.session_state: st.session_state['data'] = None
if 'dept' not in st.session_state: st.session_state['dept'] = 'General'

# 4. Sidebar - Define 'choice' FIRST
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep", "Meridian Co-Pilot"]
    choice = st.radio("Navigation", menu)

# 5. Main Logic Chain - MUST START WITH 'if'
st.title(f"Meridian Ops: {choice}")

if choice == "Data Sanitizer":
    st.subheader("Autonomous Data Intake")
    uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])
    if uploaded:
        df = pd.read_csv(uploaded) if uploaded.name.endswith('.csv') else pd.read_excel(uploaded)
        st.session_state['data'] = df
        cols = [c.lower() for c in df.columns]
        if any(x in cols for x in ['revenue', 'sales', 'profit', 'margin']): st.session_state['dept'] = 'Sales'
        elif any(x in cols for x in ['salary', 'employee', 'hiring', 'attendance']): st.session_state['dept'] = 'HR'
        elif any(x in cols for x in ['budget', 'approval', 'tax', 'cost']): st.session_state['dept'] = 'Finance'
        else: st.session_state['dept'] = 'General'
        st.success(f"Data ingested. Profile: {st.session_state['dept']}")

elif choice == "Dashboard Builder":
    if st.session_state['data'] is None:
        st.warning("Please visit 'Data Sanitizer' first.")
    else:
        df = st.session_state['data']
        dept = st.session_state['dept']
        st.subheader(f"{dept} Analytics")
        x = st.selectbox("X-Axis", df.columns)
        y = st.selectbox("Y-Axis", df.columns)
        st.plotly_chart(px.bar(df, x=x, y=y, template="plotly_white"), use_container_width=True)

elif choice == "SOP/Policy Library":
    st.subheader("Operational Playbook Registry")

elif choice == "Insights":
    st.subheader("Business Case Studies")

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing Mode")
    if st.session_state['data'] is not None:
        if st.button("Generate Presentation"): st.success("Presentation generated.")
    else: st.warning("Data required.")

elif choice == "Meridian Co-Pilot":
    st.subheader("Meridian Co-Pilot (AI Consultant)")
    if st.session_state['data'] is not None:
        query = st.text_input("Ask your Co-Pilot about this data:")
        if query:
            st.info("Analyzing via LLM Orchestration...")
            # Placeholder for OpenAI logic
            st.write(f"Co-Pilot Response to: '{query}'")
    else:
        st.warning("Data required.")
