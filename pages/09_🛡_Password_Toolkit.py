import hydralit_components as hc
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from core.pwk import new_password, password_entropy

st.set_page_config(
    page_title="Password toolkit | Haven",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

theme_bad = {
    "bgcolor": "#f8b8b4",
    "title_color": "#ED4337",
    "content_color": "#ED4337",
    "icon_color": "#ED4337",
    "icon": "fa fa-times-circle",
}
theme_neutral = {
    "bgcolor": "#eeeeee",
    "title_color": "#898e8c",
    "content_color": "#898e8c",
    "icon_color": "#898e8c",
    "icon": "fa fa-face-meh",
}
theme_good = {
    "bgcolor": "#92ebc2",
    "title_color": "#198754",
    "content_color": "#198754",
    "icon_color": "#198754",
    "icon": "fa fa-check-circle",
}

st.title("Password Toolkit")
with st.expander("Password Generator", expanded=True):
    st.write(
        """
    This tool generates a random password of a given length.
    """
    )
    length = st.slider(
        label="Password Length",
        min_value=8,
        max_value=32,
        value=16,
        step=1,
        help="Length of the password to be generated",
    )

    cols = st.columns(4)
    with cols[0]:
        lowercase = st.checkbox("lowercase", value=True)
    with cols[1]:
        uppercase = st.checkbox("uppercase", value=True)
    with cols[2]:
        numbers = st.checkbox("numbers", value=True)
    with cols[3]:
        specials = st.checkbox("special characters", value=True)

    if st.button("Generate Password"):
        st.info(new_password(length, lowercase, uppercase, numbers, specials))

with st.expander("Password Strength Checker"):
    st.write("This tool checks the strength of a password.")
    password = st.text_input(
        label="Enter password",
        placeholder="Enter password",
        type="password",
        help="Enter password to be checked",
    )

    if st.button("Check Password Strength"):
        E = password_entropy(password)

        if password is not None:
            st.info(f"Password Entropy: {E}")

            col1, col2 = st.columns(2)
            with col1:
                if E < 35:
                    hc.info_card(
                        title="Terrible",
                        content="This passwords would take get cracked INSTANTLY.",
                        sentiment="bad",
                        theme_override=theme_bad,
                        bar_value=int(E),
                    )
                elif E < 40:
                    hc.info_card(
                        title="Bad",
                        content="This passwords would take < 1 MINUTE to crack.",
                        sentiment="bad",
                        theme_override=theme_bad,
                        bar_value=int(E),
                    )
                elif E < 70:
                    hc.info_card(
                        title="Neutral.",
                        content="This passwords would take hours to crack.",
                        sentiment="neutral",
                        theme_override=theme_neutral,
                        bar_value=int(E),
                    )
                elif E < 90:
                    hc.info_card(
                        title="Great!",
                        content="This passwords would take decades to crack.",
                        sentiment="good",
                        theme_override=theme_good,
                        bar_value=int(E),
                    )
                else:
                    hc.info_card(
                        title="Brilliant!!",
                        content="This passwords would take millenniums to crack.",
                        sentiment="good",
                        theme_override=theme_good,
                        bar_value=int(E),
                    )
            with col2:
                theme_warn = theme_bad
                theme_warn["icon"] = "fa fa-exclamation-triangle"
                if password in pd.read_csv("./static/common.txt")["Passwords"]:
                    hc.info_card(
                        title="Common",
                        content="This password is commonly used.",
                        sentiment="bad",
                        theme_override=theme_warn,
                    )
                else:
                    hc.info_card(
                        title="Uncommon",
                        content="This password is uncommon.",
                        sentiment="good",
                        theme_override=theme_good,
                    )
            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number+delta",
                    value=E,
                    domain={"x": [0, 1], "y": [0, 1]},
                    title={"text": "Password Entropy"},
                    delta={"reference": 80},
                    gauge={
                        "axis": {"range": [0, 120]},
                        "bar": {"color": "#BD93FF"},
                        "borderwidth": 2,
                        "bordercolor": "#44475A",
                        "steps": [
                            {"range": [0, 45], "color": "#ED4337"},
                            {"range": [45, 80], "color": "#FFCC00"},
                            {"range": [80, 121], "color": "#198754"},
                        ],
                        "threshold": {
                            "line": {
                                "color": "black",
                                "width": 5,
                            },
                            "thickness": 1.0,
                            "value": 120,
                        },
                    },
                )
            )
            st.plotly_chart(fig)

with st.expander("Read more..."):
    st.markdown(open("blogs/Password-Toolkit.md").read())
