import streamlit as st
import hashlib

# Hash password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hardcoded credentials (change to your preferred username/password hash)
USERNAME = "selvaganesh"
PASSWORD_HASH = "e0e6097a6f8af07daf5fc7244336ba37133713e5dfb5e7b7d518a7ac9fae7e59"  # ← hash for "supersecret"

def check_login(username, password):
    return username == USERNAME and hash_password(password) == PASSWORD_HASH

def show_login():
    st.title("🔐 Login to Access AI Tools")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        if check_login(username, password):
            st.success("✅ Login successful!")
            st.session_state["authenticated"] = True
        else:
            st.error("❌ Invalid username or password.")
