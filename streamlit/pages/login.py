import os
import requests
from dotenv import load_dotenv
import streamlit as st

# Predefined credentials for simplicity
# (Replace with your authentication mechanism as needed)
USER_CREDENTIALS = {
    "admin": "password123",
    "user1": "welcome2024",
}

st.set_page_config(
    page_title="Login Page",
    initial_sidebar_state="collapsed"
)

# Main Streamlit app
def main():
    st.title("Login Page")

    # User input fields
    username = st.text_input("Username", key="uname")
    password = st.text_input("Password", type="password", key="pword")

    # Handle login
    if st.button("Login", key="login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success(f"Welcome, {username}!")
            # Store the username in the session state
            st.session_state.username = username
            st.switch_page("pages/user_landing.py")
        else:
            st.error("Invalid username or password!")

    # Create user button
    if st.button("Create User", key="create_user"):
        st.switch_page("pages/create_user.py")  # Redirect to the create user page

if __name__ == "__main__":
    main()