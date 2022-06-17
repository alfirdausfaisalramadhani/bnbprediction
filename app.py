import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()

st.header('PREDIKSI HARGA COIN BNB-USD')


# Add all your application here
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #FF4B4B;">
  <a class="navbar-brand" href="#" target="_blank">PREDIKSI BINANCE COIN</a>
</nav>
""", unsafe_allow_html=True)

app.add_app("BERANDA", home.app)
app.add_app("PREDIKSI", data.app)
app.add_app("VIDEO SEPUTAR BINANCE", model.app)
# The main app
app.run()

# st.markdown("""
# <footer class="footer bg-danger py-4">
#   <div class="container"><div class=" text-center text-white">Alfirdaus Faisal Ramadhani - Copyright©2022</div></div>
# </footer>
# """, unsafe_allow_html=True)