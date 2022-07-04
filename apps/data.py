import streamlit as st
from datetime import date

import numpy as np
import pandas as pd
from sklearn import datasets

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from prophet.plot import plot_cross_validation_metric
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics

def app():
    
    #Scrapping data dari yahoo finance
    START = "2017-05-21"
    TODAY = date.today().strftime("%Y-%m-%d")
 
    #Coin yang akan di input
    stocks = ('BNB-USD', 'NEAR-USD', 'FTM-USD', 'GMT-USD', 'ADA-USD', 'LIT-USD', 'YRT-USD', )
    selected_stock = st.selectbox('Prediksi Data', stocks)

    #Lama durasi prediksi
    n_years = st.slider('Pilih berapa tahun untuk prediksi:', 1, 5)
    period = n_years * 365

    #cache data sehingga sistem tak perlu mengunduh data ulang
    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    #Memuat data scrapping
    data_load_state = st.text('Memuat Data...') 
    data = load_data(selected_stock)
    data_load_state.text('Memuat Data, harap tunggu hingga selesai.')

    st.subheader('Data Harga ')
    st.write(data.tail())

    #Kode data harga sekarang
    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
        
    plot_raw_data()

    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    #Kode hasil prediksi prophet
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.subheader('Prediksi Data')
    st.write(forecast.tail())

    st.write('Plot Prediksi untuk {n_years} Tahunan')
    fig1 = plot_plotly(m, forecast)
    fig1.update_layout(
                xaxis_rangeselector_font_color='black',
                xaxis_rangeselector_activecolor='#FF4B4B',
                xaxis_rangeselector_bgcolor='#FFFFFF',
                )
    st.plotly_chart(fig1)
    st.subheader('Komponen Prediksi')
    fig2 = m.plot_components(forecast)
    st.write(fig2)
    
    st.subheader('Prediksi Grafik MAPE')
    df_cv = cross_validation(m, initial='730 days', period='180 days', horizon = '365 days')
    fig3 = plot_cross_validation_metric(df_cv, metric='mape')
    df_p = performance_metrics(df_cv)
    df_p.head()
    st.write(fig3)
    
    st.subheader("Tabel Cross Validation")
    st.code(df_p)
