import streamlit as st
from streamlit_option_menu import option_menu
import login
import openai
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import initialize_app, delete_app, get_app
from firebase_admin import credentials
from firebase_admin import db
from user import *
from streamlit_modal import Modal

cred = credentials.Certificate("softwareengineeringproje-30cbf-firebase-adminsdk-ubktw-48450c6b23.json")
databaseURL= "https://softwareengineeringproje-30cbf-default-rtdb.firebaseio.com/"

try:
    app = get_app()
except ValueError:
    app = firebase_admin.initialize_app(cred, {'databaseURL':databaseURL})

ref = db.reference("/") # set reference to the root of the database (or you could also set it to a key value or child key value)
users_ref = ref.child('users')
current_user_username = "sasheo"
current_user_data = users_ref.child(current_user_username).get()
current_user = Student.load_user_from_json(current_user_username,current_user_data)

def update_user_profile():
    current_user.set_classification(st.session_state.classification_input)
    current_user.set_major(st.session_state.major_input)
    current_user.set_minor(st.session_state.minor_input)
    current_user.update_values_in_firebase(users_ref)

def update_user_password():
    if st.session_state.confirm_new_password==st.session_state.new_password and st.session_state.new_password:
        changed = current_user.update_password(users_ref, st.session_state.old_password, st.session_state.new_password)
    if changed:
        st.success("Password Updated successfully")
    else:
        st.error("New passwords do not match or Wrong Old password entered")

def main_app():
    st.set_page_config(page_title="Bison Advisor", layout="wide")
    user_details = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    }

    load_dotenv()  # Load environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")
    profile_image_url = "Unknown"  # Replace with the actual path or URL
    
    with st.sidebar:
        selected = option_menu("Main Menu", 
                            ["My Profile", 'ChatBot', 'Registration Form Generator', 'Checklist', 'Self Service Resources'], 
                            icons=['file-person', 'chat-dots', 'file-earmark-text', 'card-checklist', 'info-circle'], 
                            menu_icon="cast", 
                            default_index=0)

    # Display different content based on the selection
    if selected == "My Profile":
        modal = Modal(key="Demo Key",title="Update Profile")
        st.header("My Profile")
        # Display the user's profile
        st.subheader("User Profile")
        col1, col2 = st.columns(2)
        with col1:  # Profile picture column
            st.image(profile_image_url, width=100)  # Adjust width as needed
        col1.metric("Name", current_user.get_firstname()+" "+current_user.get_lastname())
        col1.metric("Classification", current_user.get_classification())
        col1.metric("Major", current_user.get_major())
        
        with col2:    
            update_profile = st.button("Update Profile")
            col2.metric("Email", current_user.get_email())
        if current_user.get_minor() != "":
            col2.metric("Minor", current_user.get_minor())
        st.text("")
        # Action Buttons
        with col1:
            change_password = st.button("Change Password")
        
        if update_profile:
            with modal.container():
                profile_form = st.form("Profile")
                profile_form.text_input("Classification", value=current_user.get_classification(), key="classification_input") # key="keyname" is needed so that the value is saved to the session. form input cannot be accessed when embedded in something else, so the values must be saved to the sessions as st.session_state.keyname
                profile_form.text_input("Major", value=current_user.get_major(), key="major_input")
                profile_form.text_input("Minor", value=current_user.get_minor(), key="minor_input")
                profile_form.form_submit_button("Save", on_click=update_user_profile)

        if change_password:
            password_form = st.form("Password")
            password_form.text_input("old password", key="old_password", type="password")
            password_form.text_input("new password", key="new_password", type="password")
            password_form.text_input("confirm new password", key="confirm_new_password", type="password")
            password_form.form_submit_button("Submit", on_click=update_user_password)
        

    if selected == "ChatBot":
        st.header("ChatBot")

        # Initialize chat history in session state if not already present
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        user_message = st.text_input("Your Message", key="user_message_input")

        if st.button("Send"):
            if user_message:  # Check if the message is not empty
                # Append user message to chat history
                st.session_state.chat_history.append(("You", user_message))

                # Prepare messages for OpenAI API
                messages = [{"role": "user", "content": user_message}]
                for message in st.session_state.chat_history:
                    messages.append({"role": "system", "content": message[1]})

                # Get response from OpenAI
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=messages
                )

                bot_response = response.choices[0].message.content

                # Append bot response to chat history
                st.session_state.chat_history.append(("Bot", bot_response))

        # Display chat history
        chat_container = st.container()
        with chat_container:
            for author, message in st.session_state.chat_history:
                st.text(f"{author}: {message}")

    

    elif selected == "Registration Form Generator":
        st.header("Registration Form Generator")

        # Search bar to search for courses
        search_query = st.text_input("Search for Courses")

        # Placeholder for search results
        search_results_container = st.container()
        with search_results_container:
        # Dummy data for course search results
            dummy_courses = ["Course 101", "Course 102", "Course 201", "Course 202"]
            if search_query:  # Check if search query is not empty
                # Filter courses based on search query (simple case-insensitive match)
                filtered_courses = [course for course in dummy_courses if search_query.lower() in course.lower()]
                for course in filtered_courses:
                    st.write(course)

        # Buttons for adding or removing courses
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Add Course"):
                st.write("Logic to add a course goes here")

        with col2:
            if st.button("Remove Course"):
                st.write("Logic to remove a course goes here")

        # Button to download the registration form
        if st.button("Download Registration Form"):
            st.write("Logic to download the registration form goes here")        

    elif selected == "Checklist":
        st.header("Checklist")
       

    elif selected == "Self Service Resources":
        st.header("Self Service Resources")
        # Displaying buttons for various resources
        st.subheader("Useful Links")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Academic Calendar"):
                st.markdown('[All Calendars](https://howard.edu/calendars)', unsafe_allow_html=True)
                st.markdown('[2023/2024](https://howard.edu/sites/home.howard.edu/files/2023-09/2023-2024%20Academic%20Calendar%209.5.23.pdf)', unsafe_allow_html=True)

        with col2:
            if st.button("Academic Policies"):
                st.markdown('[Academic Policies](https://business.howard.edu/students/undergraduate-academic-policies)', unsafe_allow_html=True)

        with col3:
            if st.button("Course Catalogs"):
                
                st.markdown('[Course Catalog (general)](https://catalogue.howard.edu/classes)', unsafe_allow_html=True)

        with col4:
            if st.button("Degree Requirements"):
                
                st.markdown('[Degree Requirements](https://catalogue.howard.edu/general-academic-information)', unsafe_allow_html=True)
        



if not st.session_state.get('logged_in', False):
    login.login_page()  # Function from login.py that displays the login interface
else:
    main_app() 
    if st.button("Log Out"):
        login.logout()
        st.rerun() 