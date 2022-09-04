import os
from time import sleep
import streamlit as st
from dotenv import load_dotenv
import polars as pl

st.set_page_config(
    page_title="Port Scanner | Secure Spark",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

load_dotenv()
VERIFIED = False

cols = st.columns([1, 3, 1])
with cols[1]:
    st.title("Password Manager")

cols = st.columns(6)
with cols[2]:
    sign_up = st.button("Sign up")
with cols[3]:
    sign_in = st.button("Sign in")

if sign_up:
    with st.form("sign-up"):
        username = st.text_input(
            label="Enter username",
            placeholder="Username",
            type="default",
            key=10,
        )
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
        if st.form_submit_button("Register"):
            if all([len(password) > 0, len(confirm) > 0, password != confirm]):
                st.error("Passwords do not match!")
            else:
                os.environ["USERNAME"] = username
                os.environ["PASSWORD"] = password
                st.success("Registered successfully")
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
            if username == os.getenv("USERNAME") and password == os.getenv("PASSWORD"):
                with st.spinner():
                    sleep(1)
                VERIFIED = True
            else:
                st.error("Wrong password")

    if VERIFIED:
        st.success("Logged in successfully")
        cols = st.columns(6)
        with cols[2]:
            add_pwd = st.button("Add Password")
        with cols[3]:
            view_pwd = st.button("View Password")
        if add_pwd:
            with st.form("Add-Password"):
                website = st.text_input(
                    label="Website name", placeholder="Website", type="default"
                )
                username = st.text_input(
                    label="Your username", placeholder="Username", type="default"
                )
                password = st.text_input(
                    label="Your password", placeholder="Password", type="password"
                )
                if st.form_submit_button("Add"):
                    df = pl.read_csv("./db/users.csv")
                    new = pl.DataFrame(
                        {
                            "website": [website.lower()],
                            "username": [username],
                            "password": [password],
                        }
                    )
                    df.extend(new)
                    df.write_csv("./db/users.csv")
        elif view_pwd:
            with st.form("View-Password"):
                website = st.text_input(
                    label="Website name", placeholder="Website", type="default"
                )
                if st.form_submit_button("Retrieve"):
                    df = pl.read_csv("./db/users.csv")
                    results = df.filter(pl.col("website") == website)
                    st.write(results.to_pandas())
