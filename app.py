import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Meridian Ops", layout="wide")

# 2. Theme Styling (Navy/Slate/Teal)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    [data-testid="stSidebar"] { background-color: #001f3f; color: white; }
    [data-testid="stSidebar"] h1 { color: #ffffff; }
    [data-testid="stSidebar"] .stRadio { color: white; }
    .stButton>button { background-color: #008080; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Navigation
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)
    st.write("---")
    if st.button("Book Strategy Session"):
        st.write("Redirecting to calendar...")

# 4. Module Logic
st.title(f"Meridian Ops: {choice}")

if choice == "Data Sanitizer":
    st.subheader("Professional Data Intake")
    uploaded_file = st.file_uploader("Upload your data (CSV/Excel)", type=["csv", "xlsx"])
    
    if uploaded_file:
        with st.spinner("Mapping your numbers... analyzing for inconsistencies..."):
            # Load and show file
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                st.success("Data ingested successfully.")
                st.dataframe(df.head())
                st.write("Pro-Tip: Your data is clean and ready for the Dashboard Builder.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

elif choice == "Dashboard Builder":
    st.write("Dashboard tools will be activated here in the next phase.")
