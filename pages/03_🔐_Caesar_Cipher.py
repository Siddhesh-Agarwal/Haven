import polars as pd
import streamlit as st

from core.caesar import decrypt, encrypt

st.set_page_config(
    page_title="Caesar Cipher | Haven",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

CHARS = r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
LENGTH = len(CHARS)


@st.cache()
def get_data():
    return pd.read_csv("./static/words.csv")


def makes_sense(text: str):
    data = get_data()
    for word in text.strip().split():
        if all([word.isalpha(), word.lower() in data["words"], len(word) > 2]):
            return True
    return False


@st.experimental_memo
def decryptor(text: str):
    shift = 0
    while True:
        # Positive shift
        decrypted = ""
        for char in text:
            decrypted += CHARS[(CHARS.find(char) + shift) % LENGTH]
        if makes_sense(decrypted):
            return decrypted

        # Negative shift
        decrypted = ""
        for char in text:
            decrypted += CHARS[(CHARS.find(char) - shift) % LENGTH]
        if makes_sense(decrypted):
            return decrypted

        shift += 1


st.title("Caesar Cipher")

# string = ""
# for i in range(34, 127):
#     string += chr(i)
# st.info(string)


with st.expander("Encrypt", expanded=True):
    input_type = st.selectbox(
        label="Select input type",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
        key=11,
    )

    if input_type == "Text":
        text = st.text_input(
            label="Enter text:",
            help="The text to encrypt.",
            placeholder="message",
            key=12,
        )
    else:
        file = st.file_uploader(
            label="Upload a file:", help="The file to encrypt.", key=13
        )
        if file is not None:
            text = file.getvalue().decode("utf-16")

    # st.write(str(text))
    shift = st.number_input(
        label="Enter a shift value:",
        step=1,
        help="Number of bits to shift each bit with.",
        key=14,
    )

    if st.button("encrypt"):
        if len(text.strip()) > 0:
            st.info(encrypt(text, shift))
        else:
            st.error("No text to encrypt.")

with st.expander("Decrypt"):
    input_type = st.selectbox(
        label="Select input type",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
        key=21,
    )

    if input_type == "Text":
        text = st.text_input(
            label="Enter text:",
            help="The text to encrypt.",
            placeholder="message",
            key=22,
        )
    else:
        file = st.file_uploader("Upload a file:", help="The file to encrypt.", key=23)
        if file is not None:
            text = file.getvalue().decrypt("utf-16")

    shift = st.number_input(
        label="Enter a shift value:",
        step=1,
        help="Number of bits to shift each bit with.",
        key=24,
    )

    if st.button("decrypt"):
        if len(text.strip()) > 0:
            st.info(decrypt(text, shift))
        else:
            st.error("No text to decrypt.")

with st.expander("AI decryptor"):
    st.warning(
        "This is a beta version of the AI decryptor. It is not ready for production use. It only supports english decoding for now"
    )

    input_type = st.selectbox(
        label="Select input type",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
        key=31,
    )

    if input_type == "Text":
        text = st.text_input("Enter text:", help="The text to encrypt.", key=32)
    else:
        file = st.file_uploader(
            label="Upload a file:", help="The file to encrypt.", key=33
        )
        if file is not None:
            text = file.getvalue().decrypt("utf-16")

    if st.button("AI decryptor"):
        if len(text.strip()) > 0:
            st.success(decryptor(text))
        else:
            st.error("No text to encrypt.")
