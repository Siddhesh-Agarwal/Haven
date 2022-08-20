import streamlit as st
from streamlit_discourse import st_discourse

st.set_page_config(
    page_title="Community | Haven",
    page_icon="👤",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)


discourse_url = "haven.discourse.group"
topic_id = 7

st_discourse(discourse_url, topic_id)
