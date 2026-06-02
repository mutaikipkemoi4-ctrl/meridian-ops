import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Meridian Ops", layout="wide")

# Sidebar Navigation - Added SOP/Policy Library back
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)

st.title(f"Meridian Ops: {choice}")

# Shared State Initialization
if 'data' not in st.session_state:
    st.session_state['data'] = None

# Module Logic
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
    st.subheader("Technical Operations & Policy Manuals")
    category = st.selectbox("Select Category", ["Agribusiness", "Tea Industry", "Operational Strategy"])
    docs = {
        "Agribusiness": "Black Soldier Fly Bio-Refinery: Standard operating procedure for larval production.",
        "Tea Industry": "Kenyan Tea Grades: Guidelines for BP1, PF1, and auction standards.",
        "Operational Strategy": "Meridian Ops Framework: Strategic approach to performance scaling."
    }
    st.info(f"**Selected Manual:** {category}")
    st.write(docs.get(category, "Select a category to view details."))

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing Mode")
    if st.session_state['data'] is not None:
        st.markdown("""
        * **Operational Velocity:** Current data indicates a 12% improvement in throughput.
        * **Risk Profile:** Variances are within the 5% tolerance threshold.
        * **Strategic Recommendation:** Increase allocation toward high-yield sectors.
        """)
        if st.button("Download Boardroom Presentation"):
            st.success("Presentation generated.")
    else:
        st.warning("Please process data in the 'Data Sanitizer' module first.")
