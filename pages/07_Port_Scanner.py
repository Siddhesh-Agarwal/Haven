import socket

import polars as pd
import streamlit as st

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


@st.experimental_memo
def scan(from_port: int, to_port: int):
    df = pd.DataFrame(columns=["port", "status"])
    for port in range(from_port, to_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                df.append(
                    {"port": port, "status": "open"}, ignore_index=True, inplace=True
                )
    return df


st.title("Port Scanner")

hostname = st.text_input(label="Enter host name")
target = socket.gethostbyname(hostname)

col = st.columns(3)
with col[0]:
    st.write("Port range")
with col[1]:
    from_port = st.number_input(label="From", min_value=0, value=0, max_value=65534)
with col[2]:
    to_port = st.number_input(
        label="To", min_value=int(from_port), max_value=65534, value=65534
    )

if st.button("Scan"):
    with st.spinner("Scanning host..."):
        try:
            scan(from_port, to_port)
        except KeyboardInterrupt:
            st.error("[ERROR]: Exiting Program!")
        except socket.gaierror:
            st.error("[ERROR]: Hostname Could Not Be Resolved!")
        except socket.error:
            st.error("[ERROR]: Server not responding!")
