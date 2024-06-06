import streamlit as st
from second import upload,build

st.title("Best Fit Resume")

if 'page' not in st.session_state:
  st.session_state.page = 'default'

# Try to load and display the image
image_path = "Data/resume.jpeg"
try:
    st.image(image_path)
except FileNotFoundError:
    st.write("Image not found. Please check the image path.")

st.markdown("""
Introducing our cutting-edge resume customization application powered by state-of-the-art Language Models (LLMs). 
Say goodbye to generic resumes that get lost in the Applicant Tracking System (ATS) abyss. Our innovative tool revolutionizes 
the job application process by seamlessly tailoring resumes to match specific job descriptions. Simply upload your resume 
and the job description, and watch as our LLMs work their magic to optimize your resume for the highest ATS ranking. 
With our application, you'll stand out to recruiters and increase your chances of landing interviews. 
Say hello to personalized career success!
""")

# Create two columns to arrange buttons horizontally
col1, col2 = st.columns(2)

# Add buttons with labels in respective columns
upload_button = col1.button("Upload", use_container_width=True)
build_button = col2.button("Build", use_container_width=True) 


# upload resume page 


# (Optional) Add logic to handle button clicks
if upload_button:
    # Your upload functionality here
    st.session_state.page = "upload"

if build_button:
    # Your build functionality here
    st.session_state.page = "build"

if st.session_state.page == 'upload':
    upload()
elif st.session_state.page == 'build':
    build()