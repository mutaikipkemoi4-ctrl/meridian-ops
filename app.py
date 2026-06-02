import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration
st.set_page_config(page_title="Meridian Ops", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)

st.title(f"Meridian Ops: {choice}")

# Phase 2 & 3: Logic
if choice == "Data Sanitizer":
    uploaded_file = st.file_uploader("Upload your data", type=["csv", "xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.success("Mapping your numbers...")
        st.session_state['data'] = df
        
        # Auto-detect department
        cols = str(df.columns.tolist()).lower()
        if 'sales' in cols or 'revenue' in cols:
            st.session_state['dept'] = 'Sales'
        elif 'finance' in cols or 'cost' in cols:
            st.session_state['dept'] = 'Finance'
        else:
            st.session_state['dept'] = 'General'
        st.write(f"Detected Department: **{st.session_state['dept']}**")

elif choice == "Dashboard Builder":
    if 'data' in st.session_state:
        dept = st.session_state.get('dept', 'General')
        st.subheader(f"{dept} Analysis Metrics")
        
        # Departmental Metric Checklist
        metrics = ["MoM Growth", "Budget Anomalies", "KPI Performance"] if dept == "Finance" else ["Product Rank", "Conversion Rate"]
        selected = st.multiselect("Select Metrics to Visualize", metrics)
        
        if selected:
            # Simple placeholder chart for the selected metric
            x_axis = st.selectbox("X-Axis", st.session_state['data'].columns)
            y_axis = st.selectbox("Y-Axis", st.session_state['data'].columns)
            fig = px.bar(st.session_state['data'], x=x_axis, y=y_axis)
            st.plotly_chart(fig)
    else:
        st.warning("Please upload data in the Sanitizer first.")
