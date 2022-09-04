from subprocess import call
from time import sleep

import streamlit as st

st.set_page_config(
    page_title="Social Scanner | Secure Spark",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.title("Social Scanner")

username = st.text_input(label="Enter username", max_chars=50, placeholder="Username")

col = st.columns(3)
with col[0]:
    full_search = st.checkbox(label="Search full database", value=False)
with col[1]:
    recursion = st.checkbox(label="Recursive search", value=False)
with col[2]:
    extraction = st.checkbox(label="Personal info gathering", value=False)

if st.button("Search"):
    if len(username.split()) == 1:
        query = ["python", "-m", "maigret", username]
        if full_search:
            query.append("-a")
        if not recursion:
            query.append("--no-recursion")
        if not extraction:
            query.append("--no-extraction")
        query.append("--pdf")
        with st.spinner("Generating report"):
            call(query)
            sleep(10)
        with open(f"./reports/report_{username}.pdf") as file:
            st.download_button(
                label="Download report", data=file, file_name=f"{username}.pdf"
            )
    else:
        st.error("Invalid Username")
