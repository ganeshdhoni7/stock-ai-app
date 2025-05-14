import streamlit as st
import hashlib

# Hash password using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hardcoded credentials (change to your preferred username/password hash)
USERNAME = "selvaganesh"
PASSWORD_HASH = "760828cc1faa4a392a2886978febc543321c4a5afd86e7b5cef0ea9eb3fca8ea"  # ← hash for "supersecret"

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
