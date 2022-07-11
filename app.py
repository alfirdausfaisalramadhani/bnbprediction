import streamlit as st
from multiapp import MultiApp
from apps import home, data, model

app = MultiApp()

st.header('PREDIKSI HARGA COIN BNB-USD')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #FF4B4B;">
  <a class="navbar-brand" target="_blank">PREDIKSI BINANCE COIN</a>
</nav>
""", unsafe_allow_html=True)

app.add_app("BERANDA", home.app)
app.add_app("PREDIKSI", data.app)
app.add_app("VIDEO SEPUTAR BINANCE", model.app)
app.run()
