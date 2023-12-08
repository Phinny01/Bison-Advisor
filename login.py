import streamlit as st

# Function to check login credentials
def check_login(username, password):
    # Replace with real checks as needed
    return username == "admin" and password == "password"

def login_page():
    st.title("Login to Bison Advisor")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            if check_login(username, password):
                # If logged in successfully, set the session state
                st.session_state['logged_in'] = True
            else:
                st.error("Incorrect username or password.")
def logout():
    # Clear or reset session state variables related to login
    st.session_state['logged_in'] = False