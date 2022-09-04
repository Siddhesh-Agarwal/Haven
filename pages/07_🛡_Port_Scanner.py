import socket

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

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

cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('closed')) {
        return {
            'color': 'white',
            'backgroundColor': 'green'
        }
    } else if (params.value.includes('open')) {
        return {
            'color': 'white',
            'backgroundColor': 'red'
        }
    }
};
"""
)


def scan(from_port: int, to_port: int) -> pd.DataFrame:
    df = pd.DataFrame(columns=["port", "status"])
    for port in range(from_port, to_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                df = df.append({"port": port, "status": "open"}, ignore_index=True)
            else:
                df = df.append({"port": port, "status": "closed"}, ignore_index=True)
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
    if hostname.strip() != "":
        with st.spinner("Scanning host..."):
            try:
                df = scan(from_port, to_port)
                gb = GridOptionsBuilder.from_dataframe(df)
                gb.configure_pagination()
                gb.configure_side_bar()
                gb.configure_column("status", cellStyle=cellsytle_jscode)
                gridOptions = gb.build()
                AgGrid(
                    data=df,
                    gridOptions=gridOptions,
                    fit_columns_on_grid_load=True,
                    theme="dark",
                    enable_enterprise_modules=True,
                    allow_unsafe_jscode=True,
                )
            except KeyboardInterrupt:
                st.error(r"[ERROR]: Exiting Program!")
            except socket.gaierror:
                st.error(r"[ERROR]: Hostname Could Not Be Resolved!")
            except socket.error:
                st.error(r"[ERROR]: Server not responding!")
    else:
        st.error(r"[ERROR]: Hostname not given")

with st.expander("Read more..."):
    st.markdown(open("blogs/Port-Scanner.md").read())
