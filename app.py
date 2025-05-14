import streamlit as st
from user_login import verify_login
import pages.fo_prediction as fo_prediction
import pages.sentiment as sentiment
import pages.strategy_analyzer as strategy_analyzer

# Session state initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login Screen
def login_screen():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if verify_login(username, password):
            st.success("✅ Login successful!")
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid username or password.")

# Main App Layout
def main_app():
    st.sidebar.title("📊 AI Stock Market Tool")
    menu = st.sidebar.selectbox("Choose a Page", ["F&O Prediction", "Sentiment Analysis", "Strategy Analyzer", "Logout"])

    if menu == "F&O Prediction":
        fo_prediction.run()
    elif menu == "Sentiment Analysis":
        sentiment.run()
    elif menu == "Strategy Analyzer":
        strategy_analyzer.run()
    elif menu == "Logout":
        st.session_state.logged_in = False
        st.rerun()

# Run App
if st.session_state.logged_in:
    main_app()
else:
    login_screen()
