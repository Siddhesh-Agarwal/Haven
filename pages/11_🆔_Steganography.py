import os
import string
from hashlib import sha3_512
from random import choice

import polars as pd
import streamlit as st
from dotenv import load_dotenv

from core.steganography import decryptor, encryptor

st.set_page_config(
    page_title="Steganography | Secure Spark",
    page_icon="🆔",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)


@st.cache
def public_key():
    """Save public key in a binary file else create a new one"""
    # check if file exists
    load_dotenv()
    if os.getenv("PUBLIC_KEY") is not None:
        KEY = [choice(string.ascii_letters + string.digits) for _ in range(32)]
        with open(".env", "w+") as f:
            f.write(f"PUBLIC_KEY={''.join(KEY).encode()}")
    return os.getenv("PUBLIC_KEY")


st.title("Image steganography")
image = st.file_uploader(
    label="Upload image here",
    type="jpg",
    accept_multiple_files=False,
    help="upload a picture to store the message",
)

# buttons for encryption and decryption
BTN_TXT = "Continue..."
cols = st.columns(6)
with cols[0]:
    encrypt = st.button("Encrypt")
with cols[1]:
    decrypt = st.button("Decrypt")

if encrypt:
    message = st.text_input("Enter message", help="Enter message to store in image")
    BTN_TXT = "Encrypt"
elif decrypt:
    BTN_TXT = "Decrypt"

PRIVATE = st.text_input(
    "Private key", help="Enter key to encrypt/decrypt message", max_chars=32
)
PUBLIC = public_key()

if st.button(BTN_TXT, key="submit-btn") and image:
    if not PRIVATE.strip():
        st.error("Enter private key")
    else:
        df = pd.read_csv("./db/db.csv")
        if encrypt:
            message = encryptor(message, PUBLIC, PRIVATE)
            df.append({"hash": sha3_512(image), "message": message}, inplace=True)
            df.write_csv("./db/db.csv")
            st.success("Your message has been secured successfully")
            st.download_button(
                label="Download image", data=image, file_name="image.jpg"
            )
        elif decrypt:
            decryptor(message, PUBLIC, PRIVATE)
            message = df.filter(pd.col("hash") == sha3_512(image))["message"]
            st.write(message)
        else:
            st.warning("Select an option")

with st.expander("Read more..."):
    st.markdown(open("blogs/steganography.md").read())
