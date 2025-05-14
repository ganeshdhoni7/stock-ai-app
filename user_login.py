import streamlit as st
import hashlib
import hashlib

# 🔐 Hardcoded credentials (hashed for security)
USERNAME = "admin"
PASSWORD_HASH = hashlib.sha256("admin@123".encode()).hexdigest()

def verify_login(username, password):
    """
    Verifies the login credentials.
    Returns True if username and password are correct, else False.
    """
    if username != USERNAME:
        return False
    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()
    return entered_password_hash == PASSWORD_HASH

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
