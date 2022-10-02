import streamlit as st

from descriptions import RESULTS

st.set_page_config(page_title="Results", page_icon="📈")
st.sidebar.markdown("""
    Developed by [Vento Aureo 🐞](https://2022.spaceappschallenge.org/challenges/2022-challenges/carrington-event/teams/vento-aureo-1/project)
""")

st.markdown(RESULTS[0])
st.image('assets/results.png')
st.markdown(RESULTS[1])
