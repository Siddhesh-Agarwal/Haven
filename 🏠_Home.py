import streamlit as st
from streamlit_player import st_player

st.set_page_config(
    page_title="Haven",
    page_icon="./static/icon.png",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.image("./static/icon.png", use_column_width="always")
st.markdown(open("./README.md").read())
st.image("./static/roadmap.png", use_column_width="always")
