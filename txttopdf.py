import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile

# Function to convert TXT content to PDF
def txt_to_pdf(input_text, output_pdf_path):
    # Create a PDF canvas
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter  # Page size is letter (8.5 x 11 inches)
    
    # Set the starting position for text
    x = 40
    y = height - 40  # Start near the top of the page
    line_height = 12  # Space between lines of text
    
    # Write each line of text from the input text to the PDF
    for line in input_text.splitlines():
        c.drawString(x, y, line)  # Draw the line of text at position (x, y)
        y -= line_height  # Move down for the next line
        if y < 40:  # If we've reached the bottom of the page, create a new page
            c.showPage()  # Create a new page
            y = height - 40  # Reset y to top for the new page

    # Save the generated PDF
    c.save()

# Streamlit UI
st.title("TXT to PDF Converter")

# File uploader to upload a TXT file
uploaded_file = st.file_uploader("Choose a TXT file", type=["txt"])

if uploaded_file is not None:
    # Read the content of the uploaded TXT file
    text_content = uploaded_file.getvalue().decode("utf-8")
    
    # Generate a temporary file for the output PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        output_pdf_path = temp_pdf.name

    # Convert the TXT content to PDF
    try:
        txt_to_pdf(text_content, output_pdf_path)
        st.write("Conversion successful!")

        # Allow user to download the generated PDF
        with open(output_pdf_path, "rb") as f:
            st.download_button("💾 Download PDF", f, file_name="converted_text.pdf")

    except Exception as e:
        st.error(f"Error: {str(e)}")
