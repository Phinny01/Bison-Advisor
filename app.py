import streamlit as st
from streamlit_option_menu import option_menu
import login
import openai
from dotenv import load_dotenv
import os



def main_app():
    current_user_username = "sasheo"
    current_user = None
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
        st.header("My Profile")
        # Display the user's profile
        st.subheader("User Profile")
        col1, col2 = st.columns(2)
        with col1:  # Profile picture column
            st.image(profile_image_url, width=100)  # Adjust width as needed
        col1.metric("Name", f"{user_details['first_name']} {user_details['last_name']}")
        with col2:    
            update_profile = st.button("Update Profile")
        col2.metric("\nEmail", user_details['email'])
        st.text("")
        # Action Buttons
        with col1:
            change_password = st.button("Change Password")

        # Handling button clicks (You need to implement the actual functionalities)
        if change_password:
            st.write("Change password functionality goes here")
        if update_profile:
            st.write("Update profile functionality goes here")
        

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
                st.write("Redirect to the Academic Calendar page (add the link or functionality)")

        with col2:
            if st.button("Academic Policies"):
                st.write("Redirect to the Academic Policies page (add the link or functionality)")

        with col3:
            if st.button("Course Catalogs"):
                st.write("Redirect to the Course Catalogs page (add the link or functionality)")

        with col4:
            if st.button("Degree Requirements"):
                st.write("Redirect to the Degree Requirements page (add the link or functionality)")
        



if not st.session_state.get('logged_in', False):
    login.login_page()  # Function from login.py that displays the login interface
else:
    main_app() 
    if st.button("Log Out"):
        login.logout()
        st.rerun() 