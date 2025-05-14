import streamlit as st
import yfinance as yf
import pandas as pd

def show_strategy_analyzer():
    st.subheader("🧠 Strategy Analyzer (Backtesting)")

    symbol = st.text_input("Stock Symbol", "RELIANCE")
    period = st.selectbox("Select Period", ["1mo", "3mo", "6mo", "1y"])
    strategy = st.selectbox("Select Strategy", ["SMA Crossover"])

    if st.button("Analyze"):
        data = yf.download(symbol + ".NS", period=period)
        data['SMA20'] = data['Close'].rolling(20).mean()
        data['SMA50'] = data['Close'].rolling(50).mean()

        data['Signal'] = 0
        data.loc[data['SMA20'] > data['SMA50'], 'Signal'] = 1
        data.loc[data['SMA20'] < data['SMA50'], 'Signal'] = -1

        st.line_chart(data[['Close', 'SMA20', 'SMA50']])
        st.dataframe(data.tail())
        st.success("✅ Strategy signals generated (1=Buy, -1=Sell)")
