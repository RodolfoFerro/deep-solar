from glob import glob
import datetime
import os

from sklearn.preprocessing import MinMaxScaler
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import tensorflow as tf
import streamlit as st
import numpy as np

from descriptions import INFO
from utils.model import load_model
from utils.data import download_data
from utils.data import load_data

st.set_page_config(page_title="Application", page_icon="💻")
st.sidebar.markdown("""
    Developed by [Vento Aureo 🐞](https://2022.spaceappschallenge.org/challenges/2022-challenges/carrington-event/teams/vento-aureo-1/project)
""")

cdf_files = glob('*.cdf')
for cdf_file in cdf_files:
    os.remove(cdf_file)
autoencoder = load_model('models/general_model.json',
                         'models/general_model.h5')
process = False

st.markdown(INFO['instructions'])
st.markdown('---')

col_left, col_right = st.columns(2)

with col_left:
    st.markdown('### 📅 Time Window Selection')

    cdf_date = st.date_input('Select day to evaluate:',
                             datetime.date(2022, 9, 17),
                             min_value=datetime.date(1994, 11, 13),
                             max_value=datetime.date(2022, 9, 17))

    initial_t = st.time_input('Select the starting time:', datetime.time(0, 8))
    ending_t = st.time_input('Select the ending time:', datetime.time(0, 9))
    st.markdown("""
        > **NOTE:**
        > - Peaks over the threshold line can be considered as possible anomalies ans may need to be checked.
        > - A possible interpretation of lower peaks is that they may represent other possibly minor space weather events.
    """)

    process = st.button("Identify anomalies 🚀")

    if initial_t > ending_t:
        st.error('The starting time must be before the ending time')

    if process:
        cdf_file = download_data(cdf_date.strftime('%Y%m%d'))
        wind_data, filtered_data = load_data(cdf_file, cdf_date,
                                             (initial_t, ending_t))
        filtered_data = filtered_data[['norm', 'BF1']].values
        wind_data = wind_data[['norm', 'BF1']].values

        filtered_data = MinMaxScaler().fit_transform(filtered_data)

        reconst = autoencoder.predict(filtered_data)
        reconst_errors = tf.keras.losses.msle(reconst, filtered_data)
        threshold = np.mean(
            reconst_errors.numpy()) + 3 * np.std(reconst_errors.numpy())

with col_right:
    st.markdown('### 📈 Anomaly detection')

    if not process:
        st.markdown('Admire this dog until you start processing data:')
        st.image("https://static.streamlit.io/examples/dog.jpg")

    if process:
        st.markdown('Feel free to zoom the plot.')
        x = np.arange(len(reconst))

        fig = make_subplots(rows=2, cols=1)
        fig.append_trace(go.Scatter(x=x,
                                    y=filtered_data[:, 1],
                                    name='Original signal',
                                    line=dict(color='royalblue', width=3)),
                         row=1,
                         col=1)
        fig.append_trace(go.Scatter(x=x,
                                    y=reconst[:, 1],
                                    name='Reconstructed signal',
                                    line=dict(width=1)),
                         row=1,
                         col=1)
        fig.append_trace(go.Scatter(x=x, y=reconst_errors, name='Errors'),
                         row=2,
                         col=1)
        fig.add_hline(y=threshold, row=2, col=1)
        fig.update_layout(autosize=False,
                          width=500,
                          height=500,
                          margin=dict(l=50, r=50, b=100, t=100, pad=4))

        st.plotly_chart(fig)
