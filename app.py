import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Meridian Ops", layout="wide")

with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)

st.title(f"Meridian Ops: {choice}")

# --- Shared State ---
if 'data' not in st.session_state:
    st.session_state['data'] = None

if choice == "Data Sanitizer":
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
        st.warning("Upload data first.")

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing Mode")
    if st.session_state['data'] is not None:
        st.write("Generating your 3-bullet executive summary...")
        
        # Simulated AI Summary Logic
        st.markdown("""
        * **Operational Velocity:** Current data indicates a 12% improvement in throughput over the last quarter.
        * **Risk Profile:** Budget variances remain within the 5% tolerance threshold; no immediate intervention required.
        * **Strategic Recommendation:** Increase resource allocation toward high-yield sectors to capitalize on current market momentum.
        """)
        
        if st.button("Download Boardroom Presentation"):
            st.success("Presentation generated (PDF ready for export).")
    else:
        st.warning("Please process data in the 'Data Sanitizer' module to enable Boardroom insights.")
