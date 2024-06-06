import streamlit as st

# Function to display the homepage
def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    if st.button("Go to Home Page"):
        st.session_state.page = "home"
    if st.button("Go to About Page"):
        st.session_state.page = "about"
    if st.button("Go to Contact Page"):
        st.session_state.page = "contact"

# Function to display the about page
def about():
    st.title("About Page")
    st.write("Welcome to the About Page!")
    if st.button("Go to Home Page"):
        st.session_state.page = "home"
    if st.button("Go to About Page"):
        st.session_state.page = "about"
    if st.button("Go to Contact Page"):
        st.session_state.page = "contact"

# Function to display the contact page
def contact():
    st.title("Contact Page")
    st.write("Welcome to the Contact Page!")
    if st.button("Go to Home Page"):
        st.session_state.page = "home"
    if st.button("Go to About Page"):
        st.session_state.page = "about"
    if st.button("Go to Contact Page"):
        st.session_state.page = "contact"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Page navigation
if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'about':
    about()
elif st.session_state.page == 'contact':
    contact()
