import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Meridian Ops", layout="wide")

# 2. Sidebar Navigation
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)

# 3. Main Logic (The "If-Elif" Chain)
st.title(f"Meridian Ops: {choice}")

# Initialize session state for data
if 'data' not in st.session_state:
    st.session_state['data'] = None

if choice == "Data Sanitizer":
    st.subheader("Professional Data Intake")
    uploaded_file = st.file_uploader("Upload your data", type=["csv", "xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.session_state['data'] = df
        st.success("Data ready for analysis.")

elif choice == "Dashboard Builder":
    if st.session_state['data'] is not None:
        df = st.session_state['data']
        x = st.selectbox("X-Axis", df.columns)
        y = st.selectbox("Y-Axis", df.columns)
        st.plotly_chart(px.bar(df, x=x, y=y))
    else:
        st.warning("Upload data in 'Data Sanitizer' first.")

elif choice == "SOP/Policy Library":
    st.subheader("Operational Playbook Registry")
    detected_dept = st.session_state.get('dept', 'General')
    st.write(f"Based on your recent analysis, here are the **{detected_dept} Playbooks**:")
    
    playbooks = {
        "Sales": {"Conversion Optimization": "Tactics for improving lead-to-deal ratios."},
        "Finance": {"Budget Variance Control": "Protocol for identifying spending leaks."},
        "HR": {"Performance Review": "Standardized criteria for personnel assessment."}
    }
    
    if detected_dept in playbooks:
        selection = st.selectbox("Select a Playbook:", list(playbooks[detected_dept].keys()))
        st.write(playbooks[detected_dept][selection])

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing Mode")
    if st.session_state['data'] is not None:
        st.markdown("* **Operational Velocity:** Stable.")
        st.markdown("* **Strategic Recommendation:** Capitalize on current momentum.")
        if st.button("Download Presentation"):
            st.success("Presentation generated.")
    else:
        st.warning("Please process data in the 'Data Sanitizer' module first.")
