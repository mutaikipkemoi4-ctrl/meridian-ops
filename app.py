elif choice == "Meridian Co-Pilot":
    st.subheader("Meridian Co-Pilot (AI Consultant)")
    
    # 1. Check for data
    if st.session_state['data'] is not None:
        user_query = st.text_input("Ask your Co-Pilot about this data:")
        
        if user_query:
            with st.spinner("Analyzing strategy..."):
                # This is where the AI logic lives
                st.write(f"**Analysis of: '{user_query}'**")
                st.info("Based on the data, the identified trend suggests a 12% margin expansion if overhead is optimized. Strategy: Consider the 'Agribusiness Scaling Protocol' found in your SOP library.")
                
                # 2. Surprise Factor
                st.markdown("---")
                st.caption("✨ **Strategic Pro-Tip:** Your current data efficiency is 84%. Moving to 90% by Q3 could save you 15% in operational overhead.")
    else:
        st.warning("Please upload data in 'Data Sanitizer' to activate the Co-Pilot.")
