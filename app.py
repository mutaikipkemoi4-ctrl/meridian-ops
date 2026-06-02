import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Meridian Ops", layout="wide", page_icon="📈")

# 2. Executive Design System
st.markdown("""
    <style>
    .stApp { background-color: #f4f6f7; color: #0a192f; }
    [data-testid="stSidebar"] { background-color: #0a192f; color: white; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] div { color: white !important; }
    h1, h2, h3 { color: #0a192f !important; font-family: 'Segoe UI', sans-serif; }
    div.stButton > button { background-color: #008080 !important; color: white !important; border: none; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize State
if 'data' not in st.session_state:
    st.session_state['data'] = None

# 4. Sidebar - Define 'choice' HERE
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)
    st.markdown("---")
    st.button("Book Strategy Session")

# 5. Main Logic - 'choice' is now defined and ready to use
st.title(f"Meridian Ops: {choice}")

if choice == "Data Sanitizer":
    st.subheader("Autonomous Data Intake")
    uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])
    if uploaded:
        st.session_state['data'] = pd.read_csv(uploaded) if uploaded.name.endswith('.csv') else pd.read_excel(uploaded)
        st.success("Data successfully sanitized.")

elif choice == "Dashboard Builder":
    if st.session_state['data'] is None:
        st.warning("⚠️ Data Not Detected. Please upload your file in the 'Data Sanitizer' module first.")
    else:
        df = st.session_state['data']
        x = st.selectbox("X-Axis", df.columns)
        y = st.selectbox("Y-Axis", df.columns)
        st.plotly_chart(px.bar(df, x=x, y=y, template="plotly_white"), use_container_width=True)

elif choice == "SOP/Policy Library":
    st.subheader("Operational Playbook Registry")
    st.write("Browse your standard operating procedures.")

elif choice == "Insights":
    st.subheader("Business Case Studies")
    st.write("Historical insights for Meridian Ops scaling.")

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing Mode")
    if st.session_state['data'] is not None:
        if st.button("Generate Presentation"):
            st.success("Presentation generated.")
    else:
        st.warning("Please upload data in the Sanitizer first.")
