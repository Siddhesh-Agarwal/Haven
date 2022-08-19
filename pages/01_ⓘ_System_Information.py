import platform

import psutil
import streamlit as st

st.title("System Information")
my_system = platform.uname()


st.code(f"System: {my_system.system}")

st.code(f"Node Name: {my_system.node}")

iRelease = my_system.release
st.code(f"Release: {iRelease}")
if iRelease < "11":
    st.warning("You are using an old version of Windows")

iVersion = my_system.version
st.code(f"Version: {iVersion}")
if iRelease == 10 and iVersion < 10240:
    st.warning("You are using an old version of Windows")

iMachine = my_system.machine
st.code(f"Machine: {iMachine}")

iProcessor = my_system.processor
st.code(f"Processor: {iProcessor}")

st.code(f"Memory: {psutil.virtual_memory()}")
