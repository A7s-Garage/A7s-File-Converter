import streamlit as st
from docx import Document
from fpdf import FPDF
import tempfile
import os



# Function to convert DOCX to PDF using python-docx and fpdf
def convert_docx_to_pdf(docx_path, pdf_path):
    try:
        # Read the DOCX file using python-docx
        doc = Document(docx_path)
        
        # Initialize FPDF for PDF creation
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Add a new page to the PDF
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Loop through paragraphs and write them to the PDF
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if text:  # Skip empty paragraphs
                pdf.multi_cell(0, 10, text)

        # Save the PDF
        pdf.output(pdf_path)
        return True
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False

# Streamlit UI
st.title("Word to PDF Converter")

# File uploader widget for Word files (with drag-and-drop support)
uploaded_file = st.file_uploader("Drag and drop a Word file (.docx) here", type=["docx"], accept_multiple_files=False)

# Set file size limit (in bytes)
MAX_FILE_SIZE_MB = 200  # Maximum file size in MB
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

# Check if a file was uploaded
if uploaded_file is not None:
    # Check the file size
    file_size = uploaded_file.size
    if file_size > MAX_FILE_SIZE_BYTES:
        st.error(f"File is too large! The maximum file size is {MAX_FILE_SIZE_MB}MB.")
    else:
        # Save the uploaded file to a temporary directory
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            docx_path = temp_file.name  # Get the absolute path of the temporary file

        st.write(f"File uploaded successfully! Converting to PDF...")

        # Prepare output file path for the PDF in the temporary directory
        output_pdf = docx_path.replace(".docx", "_converted.pdf")

        # Start the conversion
        success = convert_docx_to_pdf(docx_path, output_pdf)

        if success:
            st.write("PDF conversion successful!")

            # Provide a download link for the converted PDF (direct download)
            if os.path.exists(output_pdf):
                with open(output_pdf, "rb") as pdf_file:
                    st.download_button(
                        label="💾 Download PDF",
                        data=pdf_file,
                        file_name="converted_document.pdf",
                        mime="application/pdf"
                    )
        else:
            st.error("An error occurred during the conversion. Please try again.")
