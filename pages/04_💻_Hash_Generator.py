import hashlib as hl
import zlib

import streamlit as st

st.set_page_config(
    page_title="Hash Generator | Secure Spark",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.title("Hash Generator")

text = st.text_input("Enter text to hash")
col1, col2 = st.columns([1, 1])

with col1:
    with st.expander("Blake-2B"):
        st.info(hl.blake2b(text.encode()).hexdigest())

    with st.expander("MD5"):
        st.info(hl.md5(text.encode()).hexdigest())

    with st.expander("SHA 224"):
        st.info(hl.sha224(text.encode()).hexdigest())

    with st.expander("SHA 256"):
        st.info(hl.sha256(text.encode()).hexdigest())

    with st.expander("SHA 384"):
        st.info(hl.sha384(text.encode()).hexdigest())

    with st.expander("SHA 512"):
        st.info(hl.sha512(text.encode()).hexdigest())

    with st.expander("SHAKE 128"):
        st.info(hl.shake_128(text.encode()).hexdigest(16))

    with st.expander("Adler 32"):
        st.info(zlib.adler32(text.encode()))
with col2:
    with st.expander("Blake-2S"):
        st.info(hl.blake2s(text.encode()).hexdigest())

    with st.expander("SHA 1"):
        st.info(hl.sha1(text.encode()).hexdigest())

    with st.expander("SHA-3 224"):
        st.info(hl.sha3_224(text.encode()).hexdigest())

    with st.expander("SHA-3 256"):
        st.info(hl.sha3_256(text.encode()).hexdigest())

    with st.expander("SHA-3 384"):
        st.info(hl.sha3_384(text.encode()).hexdigest())

    with st.expander("SHA-3 512"):
        st.info(hl.sha3_512(text.encode()).hexdigest())

    with st.expander("SHAKE 256"):
        st.info(hl.shake_256(text.encode()).hexdigest(32))

    with st.expander("CRC 32"):
        st.info(zlib.crc32(text.encode()))

with st.expander("Read more..."):
    st.markdown(open("docs/Hash.md").read())
