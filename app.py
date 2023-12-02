import streamlit as st
from streamlit_option_menu import option_menu # check here https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514

current_user_username = "sasheo" # we're only building for one user. Next, log in/user authentication will be enabled and this will not be static
current_user = None
st.set_page_config(page_title="Bison Advisor", layout="wide")

st.title("My Profile")
st.subheader(current_user_username)


with st.sidebar:
    selected = option_menu("Main Menu", ["My Profile", 'ChatBot', 'Registration Form Generator', 'Checklist', 'Self Service Resources'], 
        icons=['file-person', 'chat-dots', 'file-earmark-text','card-checklist', 'info-circle'], menu_icon="cast", default_index=1) # icons check here https://icons.getbootstrap.com/?q=chat
    selected

# check here: update profile/inputs textboxes radio buttons etc on page https://www.datacamp.com/tutorial/streamlit