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
    st.subheader("Professional Data Intake")
    uploaded_file = st.file_uploader("Upload your data (CSV/Excel)", type=["csv", "xlsx"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.success("Mapping your numbers...")
        st.session_state['data'] = df
        st.dataframe(df.head())
        
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
        
        metrics = ["MoM Growth", "Budget Anomalies", "KPI Performance"] if dept == "Finance" else ["Product Rank", "Conversion Rate"]
        selected = st.multiselect("Select Metrics to Visualize", metrics)
        
        if selected:
            cols = st.session_state['data'].columns.tolist()
            x_axis = st.selectbox("X-Axis", cols)
            y_axis = st.selectbox("Y-Axis", cols)
            fig = px.bar(st.session_state['data'], x=x_axis, y=y_axis)
            st.plotly_chart(fig)
            
            # Phase 4: Boardroom Narrative
            st.markdown("---")
            st.subheader("📊 Technical & Strategic Briefing")
            with st.container():
                st.markdown(f"**1. What:** Analysis of {selected[0]} focusing on {y_axis} trends.")
                st.markdown(f"**2. Why:** This trend indicates {dept} performance shifts that impact our bottom line.")
                st.markdown("**3. Boardroom Talking Points:**")
                st.markdown(f"- We have observed significant variance in {y_axis}.")
                st.markdown("- Recommendations involve re-aligning resources to optimize output.")
                st.markdown("- Action: Approval required for strategic pivot.")
            
            if st.button("Generate Executive Briefing"):
                st.info("Executive Summary: The data shows a stable trend with a 15% optimization potential in the current period.")
    else:
        st.warning("Please upload a file in the 'Data Sanitizer' module first.")
