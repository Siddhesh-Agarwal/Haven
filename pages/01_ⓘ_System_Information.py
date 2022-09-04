import platform

import streamlit as st

st.set_page_config(
    page_title="System Info | Secure Spark",
    page_icon=":desktop_computer:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.title("System Information")
my_system = platform.uname()

st.info(f"**System**: {my_system.system}")

st.info(f"**Node Name**: {my_system.node}")

iRelease = my_system.release
st.info(f"**Release**: {iRelease}")
if iRelease < "11":
    st.warning("You are using an old version of Windows")

iVersion = my_system.version

st.info(f"**Version**: {iVersion}")
if iRelease == 10 and iVersion < 10240:
    st.warning("You are using an old version of Windows")

iMachine = my_system.machine
st.info(f"**Machine**: {iMachine}")

iProcessor = my_system.processor
st.info(f"**Processor**: {iProcessor}")
