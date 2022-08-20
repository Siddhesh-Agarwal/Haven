from hashlib import sha3_512
import pandas as pd
import os
import streamlit as st
from secrets import choice
from core.pwk import check_username, generate_salt
from dotenv import load_dotenv

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
load_dotenv()
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
            salt = generate_salt()
            pepper = os.getenv("PEPPER")
            password = password + pepper + salt
            df.append(
                {
                    "username": username,
                    "password": sha3_512(password.encode()).hexdigest(),
                    "salt": salt,
                }
            )
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

        if st.form_submit_button("Sign in"):
            df = pd.read_csv("./db/users.csv")
            salt = df.loc[df["username"] == username, "salt"].values[0]
            pepper = os.getenv("PEPPER")
            password = password + pepper + salt
            if (
                df.loc[df["username"] == username, "password"].values[0]
                == sha3_512(password.encode()).hexdigest()
            ):
                st.success("You are signed in!")
                USERNAME = username
            else:
                st.error("Invalid username or password!")
                USERNAME = None

if USERNAME is not None:
    # password manager for user
    pass
