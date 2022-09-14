import streamlit as st
from cryptmoji import Cryptmoji

st.set_page_config(
    page_title="Emoji Crypt | Secure Spark",
    page_icon="😄",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.title("Emoji Crypt")

with st.expander("Encrypt", expanded=True):
    text = st.text_area("Text to encrypt", key=10, max_chars=32)
    keyword = st.text_input("Keyword", value="random_string", key=11)
    if st.button("Encrypt"):
        if keyword.strip() != "" and text.strip() != "":
            EC = Cryptmoji(text, keyword)
            st.write(EC.encrypt())
        else:
            st.error("Bruh, just fill both of them.")

with st.expander("Decrypt", expanded=False):
    text = st.text_area("Text to decrypt", key=20, max_chars=32)
    keyword = st.text_input("Keyword", value="random_string", key=21)
    if st.button("Decrypt"):
        if keyword.strip() != "" and text.strip() != "":
            EC = Cryptmoji(text, keyword)
            st.write(EC.decrypt())
        else:
            st.error("Bruh, just fill both of them.")
