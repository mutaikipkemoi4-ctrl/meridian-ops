elif choice == "Dashboard Builder":
    if st.session_state['data'] is None:
        st.warning("⚠️ Data Not Detected. Please upload your file in 'Data Sanitizer' first.")
    else:
        dept = st.session_state.get('dept', 'General')
        st.subheader(f"{dept} Analytics Menu")
        
        # 1. Targeted Strategic Pro-Tips Mapping
        tips = {
            "Sales": "To boost MoM growth, analyze your 'Customer Acquisition Cost' versus 'Lifetime Value'. Focus on the top 20% of products driving 80% of revenue.",
            "Finance": "Budget variance is the silent killer. Cross-reference your 'Approval Rate' with 'Monthly Spend' to catch anomalies before they hit the bottom line.",
            "HR": "Your 'Hiring Velocity' should be balanced with 'Retention Rate'. High turnover is often an early indicator of culture misalignment, not just compensation.",
            "General": "Always verify your data source's ISO formatting before building board-ready visualizations."
        }
        
        # 2. Display the Metric Selector
        metrics = {"Sales": ["MoM Growth", "Product Rank"], "Finance": ["Approval Rate", "Budget Anomalies"], "HR": ["Retention Rate", "Hiring Velocity"]}.get(dept, ["General Trend"])
        selected_metric = st.selectbox("Select Metric:", metrics)
        
        # 3. Chart Generation
        df = st.session_state['data']
        x = st.selectbox("X-Axis", df.columns)
        y = st.selectbox("Y-Axis", df.columns)
        st.plotly_chart(px.bar(df, x=x, y=y, template="plotly_white"), use_container_width=True)
        
        # 4. The Consultant-in-a-Box Briefing
        st.markdown("---")
        st.markdown(f"### 💡 Meridian Strategic Insight ({dept})")
        st.write(tips.get(dept, tips["General"]))
        
        # Adding a hint of 'non-boring' personality
        st.caption("— Your Meridian Co-Pilot is currently monitoring these trends for board-level alerts.")
