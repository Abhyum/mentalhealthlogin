import streamlit as st
import json
import pyrebase

# Load Firebase config from Streamlit Secrets
firebase_config = json.loads(st.secrets["FIREBASE_CONFIG"])

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Streamlit Page Setup
st.set_page_config(page_title="Login | Mood Journal", layout="centered")
st.title("🔐 Mood & Emotion Journal Login")

# UI Elements
action = st.selectbox("Choose Action", ["Login", "Register"])
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if action == "Register":
    if st.button("Create Account"):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("✅ Account created. Please log in.")
        except Exception as e:
            st.error(f"Registration failed: {e}")

if action == "Login":
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("🎉 Login successful! Redirecting...")
            # Optional manual redirect
            st.markdown("[Click here if you are not redirected](https://w9lpq8ji6knqtc7wqnvixv.streamlit.app/)")
            # Automatic redirect (1-second delay)
            st.components.v1.html("""
                <meta http-equiv="refresh" content="1;url=https://w9lpq8ji6knqtc7wqnvixv.streamlit.app/">
            """, height=0)
        except Exception as e:
            st.error(f"Login failed: {e}")
