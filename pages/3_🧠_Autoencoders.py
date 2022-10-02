import streamlit as st

from utils.descriptions import AUTOENCODERS
from utils.descriptions import AUTOENCODERS_IMGS

st.set_page_config(page_title="Autoencoders", page_icon="🧠")
st.sidebar.markdown("""
    Developed by [Vento Aureo 🐞](https://2022.spaceappschallenge.org/challenges/2022-challenges/carrington-event/teams/vento-aureo-1/project)
""")

st.markdown(AUTOENCODERS[0])
st.image(AUTOENCODERS_IMGS[0], width=200, output_format='PNG')
st.markdown(AUTOENCODERS[1])
st.image(AUTOENCODERS_IMGS[1], width=120)
st.markdown(AUTOENCODERS[2])
st.image(AUTOENCODERS_IMGS[2], width=90)
st.markdown(AUTOENCODERS[3])
st.image(AUTOENCODERS_IMGS[3], width=400)
st.markdown(AUTOENCODERS[4])
