import streamlit as st

def upload():
    uploaded_file = st.file_uploader("Upload Resume")

    if uploaded_file is not None:
        # Get filename and potentially save the file (optional)
        filename = uploaded_file.name
        # Optionally save the file (replace with your desired location)
        # with open(f"uploads/{filename}", "wb") as f:
        #     f.write(uploaded_file.getvalue())

        st.write(f"File uploaded: {filename}")


# Build resume page 
def build():
    pass
