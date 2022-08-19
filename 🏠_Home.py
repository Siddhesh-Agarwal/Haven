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

# st.image("./static/icon.png", use_column_width="always")


st.markdown(open("./README.md").read())

with st.expander("Image Steganography"):
    pass

with st.expander("Caesar Cipher System"):
    pass

with st.expander("DDoS Attacks"):
    pass

with st.expander("Keylogger"):
    pass

with st.expander("Hash generator"):
    st_player("https://youtu.be/QbkHUs8pFMU")

with st.expander("Social Scrapper"):
    pass

with st.expander("Port scanner"):
    pass

with st.expander("Password generator and password strength"):
    pass
