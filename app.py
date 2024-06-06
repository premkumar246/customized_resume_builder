import streamlit as st
from docx import Document

def read_docx(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def main():
    st.title("Resume Viewer")

    uploaded_file = st.file_uploader("Choose a resume file", type=["txt", "docx"])
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            # Read text file
            resume_text = uploaded_file.read().decode("utf-8")
            st.text_area("Resume Content", resume_text, height=500)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            # Read docx file
            resume_text = read_docx(uploaded_file)
            st.text_area("Resume Content", resume_text, height=500)

if __name__ == "__main__":
    main()
