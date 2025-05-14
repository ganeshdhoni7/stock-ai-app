import streamlit as st
from user_login import verify_login
import pages.fo_prediction as fo_prediction
import pages.sentiment as sentiment
import pages.strategy_analyzer as strategy_analyzer


# Initialize session state on first load
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login block
if not st.session_state.logged_in:
    st.title("📊 AI Stock Market Dashboard Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if verify_login(username, password):
            st.success("✅ Login successful!")
            st.session_state.logged_in = True
            st.rerun()  # 🔁 rerun to show the app after login
        else:
            st.error("❌ Invalid username or password.")

# After login
if st.session_state.logged_in:
    st.sidebar.success("👋 Welcome, Selvaganesh!")
    
    page = st.sidebar.selectbox("📂 Choose a Page", [
        "Home", 
        "F&O Prediction", 
        "Strategy Analyzer", 
        "Sentiment Analysis", 
        "Live Charts"
    ])

    if page == "Home":
        st.title("📈 AI Stock Dashboard")
        st.markdown("Welcome to your private AI dashboard. Select a function from the left.")
    
 elif menu == "F&O Prediction":
    fo_prediction.run()
 elif menu == "Sentiment Analysis":
    sentiment.run()
 elif menu == "Strategy Analyzer":
    strategy_analyzer.run()


