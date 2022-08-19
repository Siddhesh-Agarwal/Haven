from hashlib import sha3_512
import pandas as pd
import streamlit as st
from secrets import choice
from core.pwk import check_username

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

st.set_page_config(
    page_title="Port Scanner | Haven",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.title("Password Manager")
cols = st.columns(6)
with cols[0]:
    sign_up = st.button("Sign up")
with cols[1]:
    sign_in = st.button("Sign in")

if sign_up:
    with st.form("sign-up"):
        username = st.text_input(
            label="Enter username",
            max_chars=50,
            placeholder="Username",
            type="default",
            key=10,
        )
        if username:
            check_username(username)

        password = st.text_input(
            label="Enter password",
            max_chars=50,
            placeholder="Password",
            type="password",
            key=11,
        )
        confirm = st.text_input(
            label="Enter password",
            max_chars=50,
            placeholder="Password",
            type="password",
            key=12,
        )
        if password != confirm:
            st.error("Passwords do not match!")

        if st.form_submit_button("Register"):
            password = password
            df = pd.read_csv("./db/users.csv")
            salt = 
            df.append({""})
elif sign_in:
    with st.form("authentication"):
        username = st.text_input(
            label="Enter username",
            max_chars=50,
            placeholder="Username",
            type="default",
            key=20,
        )

        password = st.text_input(
            label="Enter password",
            max_chars=50,
            placeholder="Password",
            type="password",
            key=21,
        )
