import streamlit as st
import pyrebase
import json
import webbrowser

# Firebase config: Load from file
with open("firebase_config.json") as f:
    firebase_config = json.load(f)

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Streamlit UI
st.set_page_config(page_title="Login to Mood Journal", layout="centered")
st.title("🔐 Mood & Emotion Journal - Login")

action = st.selectbox("Choose Action", ["Login", "Register"])

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if action == "Register":
    if st.button("Create Account"):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("✅ Account created. Please login now.")
        except Exception as e:
            st.error(f"Registration failed: {e}")

if action == "Login":
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("🎉 Logged in successfully!")
            st.markdown("[Click here to open your Mood Journal](https://w9lpq8ji6knqtc7wqnvixv.streamlit.app/)")
            st.balloons()
        except Exception as e:
            st.error(f"Login failed: {e}")
