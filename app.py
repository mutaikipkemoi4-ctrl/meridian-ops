elif choice == "SOP/Policy Library":
    st.subheader("Operational Playbook Registry")
    
    # Logic: If we already detected a department from the Data Sanitizer, 
    # suggest the most relevant playbook automatically.
    detected_dept = st.session_state.get('dept', 'General')
    st.write(f"Based on your recent analysis, here are the **{detected_dept} Playbooks**:")
    
    playbooks = {
        "Sales": {
            "Conversion Optimization": "Tactics for improving lead-to-deal ratios.",
            "Pipeline Hygiene": "Steps to clean and prioritize your sales funnel."
        },
        "Finance": {
            "Budget Variance Control": "Protocol for identifying and correcting spending leaks.",
            "Cash Flow Management": "Strategies for optimizing working capital."
        },
        "HR": {
            "Performance Review Framework": "Standardized criteria for personnel assessment.",
            "Conflict Resolution": "Step-by-step guide for mediation."
        }
    }
    
    # Allow user to pick from recommended playbooks
    if detected_dept in playbooks:
        selection = st.selectbox("Select a Playbook to implement:", list(playbooks[detected_dept].keys()))
        st.success(f"Implementing: {selection}")
        st.write(playbooks[detected_dept][selection])
    else:
        st.info("No specific department detected. View all standard operational protocols below.")
