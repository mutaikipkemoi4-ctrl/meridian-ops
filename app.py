# --- 1. SET UP THE SIDEBAR ---
with st.sidebar:
    menu = ["Data Sanitizer", "Dashboard Builder", "SOP/Policy Library", "Insights", "Boardroom Prep", "Meridian Co-Pilot"]
    choice = st.radio("Navigation", menu)

# --- 2. START THE MASTER SWITCH ---
# Every logic block must be indented under this single sequence
if choice == "Data Sanitizer":
    # Your code for Sanitizer
    pass

elif choice == "Dashboard Builder":
    # Your code for Dashboard
    pass

elif choice == "SOP/Policy Library":
    # Your code for SOP
    pass

elif choice == "Insights":
    # Your code for Insights
    pass

elif choice == "Boardroom Prep":
    # Your code for Boardroom
    pass

elif choice == "Meridian Co-Pilot":
    # Your code for Co-Pilot
    pass
