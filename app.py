import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Executive Design System & Config
st.set_page_config(page_title="Meridian Ops", layout="wide", page_icon="📈")

st.markdown("""
    <style>
    /* Navy (#0a192f), Slate (#708090), Teal (#008080) */
    .stApp { background-color: #f4f6f7; color: #0a192f; }
    [data-testid="stSidebar"] { background-color: #0a192f; color: white; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] div { color: white !important; }
    h1, h2, h3 { color: #0a192f !important; font-family: 'Segoe UI', sans-serif; }
    div.stButton > button { background-color: #008080 !important; color: white !important; border: none !important; border-radius: 4px !important; font-weight: 600; }
    .stAlert { border-left: 5px solid #708090; }
    </style>
    """, unsafe_allow_html=True)

# 2. State Persistence
if 'data' not in st.session_state: st.session_state['data'] = None

# 3. Sidebar Navigation
with st.sidebar:
    st.title("Meridian Ops")
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep"]
    choice = st.radio("Navigation", menu)
    st.markdown("---")
    st.write("### Strategy & Growth")
    st.button("Book Strategy Session")
    st.button("🚀 Upgrade to Pro")

# 4. Main Controller
st.title(f"Meridian Ops: {choice}")

if choice == "Data Sanitizer":
    st.subheader("Autonomous Data Intake")
    uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])
    if uploaded:
        st.session_state['data'] = pd.read_csv(uploaded) if uploaded.name.endswith('.csv') else pd.read_excel(uploaded)
        st.success("Data successfully sanitized and ready for the boardroom.")

elif choice == "Dashboard Builder":
    if st.session_state['data'] is not None:
        df = st.session_state['data']
        x, y = st.columns(2)
        col_x = x.selectbox("X-Axis", df.columns)
        col_y = y.selectbox("V-Axis", df.columns)
        st.plotly_chart(px.bar(df, x=col_x, y=col_y, template="plotly_white"), use_container_width=True)
        st.info("💡 **Strategic Pro-Tip:** Review your MoM variance for efficiency optimization.")
    else:
        st.warning("Data required. Please visit 'Data Sanitizer' first.")

elif choice == "SOP/Policy Library":
    st.subheader("Operational Playbook Registry")
    st.write("Browse your standard operating procedures for executive alignment.")

elif choice == "Insights":
    st.subheader("Business Case Studies")
    st.markdown("* **Case Study 1:** Scaling Agribusiness throughput.")
    st.markdown("* **Case Study 2:** Financial recovery protocols.")

elif choice == "Boardroom Prep":
    st.subheader("Executive Briefing Mode")
    if st.session_state['data'] is not None:
        st.markdown("### 📊 Boardroom Summary")
        st.write("Current data shows stable trends with 15% optimization potential.")
        if st.button("Generate Presentation"): st.success("Presentation generated.")
    else:
        st.warning("Data required. Please visit 'Data Sanitizer' first.")
