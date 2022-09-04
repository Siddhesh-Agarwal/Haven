import streamlit as st

st.set_page_config(
    page_title="Secure Spark",
    page_icon="./static/logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

# st.image("./static/logo.png", use_column_width="always")
st.markdown(open("./README.md").read())
st.image("./static/roadmap.png", use_column_width="always")
