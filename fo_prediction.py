import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

def show_fo_prediction():
    st.subheader("🔮 F&O Option Price Prediction")

    symbol = st.text_input("Enter Stock Symbol (e.g., INFY)", "INFY")
    days_ahead = st.slider("Days Ahead to Predict", 1, 10, 5)

    if st.button("Predict"):
        data = yf.download(symbol + ".NS", period="6mo")
        data['Target'] = data['Close'].shift(-days_ahead)
        data.dropna(inplace=True)

        X = np.arange(len(data)).reshape(-1, 1)
        y = data['Target'].values

        model = LinearRegression()
        model.fit(X, y)
        future_index = np.array([[len(data) + days_ahead]])
        prediction = model.predict(future_index)[0]

        st.success(f"📈 Predicted Price after {days_ahead} days: ₹{prediction:.2f}")
        st.line_chart(data['Close'])
