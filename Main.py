import streamlit as st

from descriptions import INFO

st.set_page_config(
    page_title="Deep Solar",
    page_icon="☀️",
)

st.write("# Welcome to Deep Solar! 👋")

st.markdown(INFO['challenge'])
st.markdown(INFO['solution'])

st.sidebar.markdown("""
    Developed by [Vento Aureo 🐞](https://2022.spaceappschallenge.org/challenges/2022-challenges/carrington-event/teams/vento-aureo-1/project)
""")
