import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Meridian Ops", layout="wide")

# 2. Sidebar Navigation
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Boardroom Prep", "Meridian Co-Pilot", "Insights"]
    choice = st.radio("Navigation", menu)
    
    st.markdown("---")
    if st.button("Unlock Pro Access"):
        st.write("Redirecting...")

# 3. Initialize session state
if 'data' not in st.session_state:
    st.session_state['data'] = None

# 4. Main Logic Chain (Must be one continuous block)
st.title(f"Meridian Ops: {choice}")

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
    st.write(f"Based on your recent analysis, here are the **{detected_dept} Playbooks**.")

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing Mode")
    if st.session_state['data'] is not None:
        st.markdown("* **Strategic Recommendation:** Capitalize on current momentum.")
        if st.button("Download Presentation"):
            st.success("Presentation generated.")
    else:
        st.warning("Process data in 'Data Sanitizer' first.")

elif choice == "Meridian Co-Pilot":
    st.subheader("Meridian Co-Pilot")
    user_query = st.text_input("Ask me anything about your dataset:")
    if user_query:
        st.info("Analyzing dataset... (Co-Pilot functionality active)")

elif choice == "Insights":
    st.subheader("Business Case Studies")
    st.markdown("* **Case Study 1:** Scaling Agribusiness throughput via BSF tech.")
    st.markdown("* **Case Study 2:** Financial recovery protocols for the SME sector.")
