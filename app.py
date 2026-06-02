elif choice == "Dashboard Builder":
    # --- Check for Data ---
    if st.session_state['data'] is None:
        st.warning("⚠️ Data Not Detected. Please upload your file in the 'Data Sanitizer' module first.")
        st.info("The Dashboard requires a dataset to generate visual insights.")
    else:
        # --- Proceed with Rendering if Data Exists ---
        df = st.session_state['data']
        st.subheader("Performance Analytics")
        
        # UI Layout for selecting axes
        col1, col2 = st.columns(2)
        x_axis = col1.selectbox("Select X-Axis", df.columns)
        y_axis = col2.selectbox("Select Y-Axis", df.columns)
        
        # Generate Chart
        fig = px.bar(df, x=x_axis, y=y_axis, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
        
        # Strategic Pro-Tip (The 'Consultant-in-a-Box' value)
        st.info("💡 **Strategic Pro-Tip:** Observe the delta between your peaks and valleys to identify potential operational bottlenecks.")
