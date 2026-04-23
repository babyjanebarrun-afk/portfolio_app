import streamlit as st

st.title("📁 My Projects")

projects = {
    "Reservation System": "Boarding House Reservation System.",
    "BL Jey Food Hub": "An online food ordering system.",
    "Portfolio Website": "Personal portfolio showcasing skills."
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)