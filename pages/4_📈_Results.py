import streamlit as st

from descriptions import RESULTS
from descriptions import RESULTS_IMGS

st.set_page_config(page_title="Results", page_icon="📈")
st.sidebar.markdown("""
    Developed by [Vento Aureo 🐞](https://2022.spaceappschallenge.org/challenges/2022-challenges/carrington-event/teams/vento-aureo-1/project)
""")

st.markdown(RESULTS[0])
st.image(RESULTS_IMGS[0], use_column_width=True)
st.markdown(RESULTS[1])
st.image(RESULTS_IMGS[2], use_column_width=True)
st.markdown(RESULTS[2])
st.image(RESULTS_IMGS[1], use_column_width=True)
st.markdown(RESULTS[3])
