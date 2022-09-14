import polars as pd
import streamlit as st

from core.logging import logger

st.set_page_config(
    page_title="Keylogger | Secure Spark",
    page_icon="⌨",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.title("Keylogger")

if st.button("Start Logger"):
    logger()

    st.subheader("Keystrokes Data")
    df = pd.read_csv("./logs/keylogs.csv")
    st.write(df.to_pandas())

with st.expander("Read more..."):
    st.markdown(open("docs/Keylogger.md").read())
