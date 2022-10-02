import streamlit as st

from descriptions import ANOMALY_DETECTION
from descriptions import ANOMALY_DETECTION_IMGS

st.set_page_config(page_title="Anomaly detection", page_icon="📊")
st.sidebar.markdown("""
    Developed by [Vento Aureo 🐞](https://2022.spaceappschallenge.org/challenges/2022-challenges/carrington-event/teams/vento-aureo-1/project)
""")

st.markdown(ANOMALY_DETECTION[0])
st.image(ANOMALY_DETECTION_IMGS[0])
st.markdown(ANOMALY_DETECTION[1])
st.image(ANOMALY_DETECTION_IMGS[1])
st.markdown(ANOMALY_DETECTION[2])
st.image(ANOMALY_DETECTION_IMGS[2])
st.markdown(ANOMALY_DETECTION[3])
