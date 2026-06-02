import openai

# You would set this in your Streamlit configuration
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

elif choice == "Meridian Co-Pilot":
    st.subheader("Meridian Co-Pilot (AI Consultant)")
    if st.session_state['data'] is not None:
        df = st.session_state['data']
        query = st.text_input("Ask your Co-Pilot about this data:")
        
        if query:
            # 1. Create a data summary for the AI
            data_summary = df.describe().to_string() 
            
            with st.spinner("Meridian is reasoning over your data..."):
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a professional, energetic executive consultant for Meridian Ops. Use the provided data summary to answer questions."},
                        {"role": "user", "content": f"Data Summary: {data_summary}\n\nUser Question: {query}"}
                    ]
                )
                st.markdown("### 🤖 Consultant Briefing")
                st.write(response.choices[0].message.content)
    else:
        st.warning("Please upload data in the Sanitizer first.")
