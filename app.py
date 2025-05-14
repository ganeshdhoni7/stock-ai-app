import streamlit as st
from user_login import show_login
from fo_prediction import show_fo_prediction
from strategy_analyzer import show_strategy_analyzer
from sentiment import show_sentiment

st.set_page_config(page_title="Stock AI Hub", layout="wide")

# --- Authenticate User ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    show_login()
    st.stop()

# --- Sidebar Navigation ---
st.sidebar.title("📊 AI Stock Tools")
menu = st.sidebar.radio(
    "Select a Feature",
    ["🏠 Home", "🔮 F&O Prediction", "🧠 Strategy Analyzer", "📰 Market Sentiment"]
)

# --- Main Area ---
st.title("🚀 AI Stock Market Website")

if menu == "🏠 Home":
    st.image("https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif", width=600)
    st.markdown("""
        ### 🔧 Features:
        - F&O Option Prediction
        - Strategy Analyzer
        - Market Sentiment from News
        - Secure Private Access
    """)

elif menu == "🔮 F&O Prediction":
    show_fo_prediction()

elif menu == "🧠 Strategy Analyzer":
    show_strategy_analyzer()

elif menu == "📰 Market Sentiment":
    show_sentiment()
