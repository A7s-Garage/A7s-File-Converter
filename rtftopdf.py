import streamlit as st
import tempfile
from striprtf.striprtf import rtf_to_text
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to convert RTF content to PDF
def rtf_to_pdf(input_rtf_path, output_pdf_path):
    # Extract text from RTF using striprtf
    with open(input_rtf_path, 'r', encoding='utf-8') as rtf_file:
        rtf_content = rtf_file.read()
    
    text_content = rtf_to_text(rtf_content)

    # Create a PDF using ReportLab
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    text_object = c.beginText(40, 750)
    text_object.setFont("Helvetica", 12)
    text_object.setTextOrigin(40, 750)

    # Add the text content to the PDF
    text_object.textLines(text_content)
    c.drawText(text_object)
    c.save()

# Streamlit UI
st.title("RTF to PDF Converter")

# File uploader to allow users to upload an RTF file
uploaded_file = st.file_uploader("Choose an RTF file", type=["rtf"])

if uploaded_file is not None:
    # Save the uploaded RTF file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".rtf") as temp_rtf:
        temp_rtf.write(uploaded_file.getbuffer())
        temp_rtf_path = temp_rtf.name

    # Define the output PDF file path
    output_pdf_path = temp_rtf_path.rsplit(".", 1)[0] + ".pdf"

    # Display message while converting
    st.write("Converting to PDF...")

    # Call the RTF to PDF conversion function
    try:
        rtf_to_pdf(temp_rtf_path, output_pdf_path)
        st.write("Conversion successful!")

        # Provide a download button for the resulting PDF
        with open(output_pdf_path, "rb") as f:
            st.download_button("💾 Download PDF", f, file_name="converted_rtf.pdf")
    except Exception as e:
        st.error(f"Error: {str(e)}")
