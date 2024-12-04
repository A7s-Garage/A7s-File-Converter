import streamlit as st
import pdfplumber
from docx import Document
import io


# Title of the app
st.title("PDF to Word Converter")

# File uploader allows PDF upload
uploaded_file = st.file_uploader("Drag and drop a PDF file", type=["pdf"], accept_multiple_files=False)

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    # Open the uploaded PDF file using pdfplumber
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# Function to convert extracted text to Word
def convert_text_to_word(text):
    doc = Document()
    doc.add_paragraph(text)  # Add the extracted text as a paragraph in the Word document
    return doc

# Check if a file has been uploaded
if uploaded_file is not None:
    # Extract text from the PDF file
    text = extract_text_from_pdf(uploaded_file)
    
    if text.strip() == "":
        st.error("No text could be extracted from the PDF. It might be an image-based PDF.")
    else:
        # Display the extracted text (for the user to review)
        st.write("Extracted Text from PDF:")
        st.text_area("Extracted Text", text, height=200)
        
        # Convert the extracted text to a Word document
        doc = convert_text_to_word(text)
        
        # Function to save the Word document in-memory
        def save_word_doc(doc):
            output = io.BytesIO()
            doc.save(output)
            output.seek(0)
            return output
        
        # Add a download button for the Word document
        st.download_button(
            label="💾 Download Word Document",
            data=save_word_doc(doc),
            file_name="converted_file.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
