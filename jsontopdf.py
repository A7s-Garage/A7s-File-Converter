import streamlit as st
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os

# Function to convert JSON data to PDF
def json_to_pdf(json_data, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    y_position = height - 40  # Start from the top of the page

    c.setFont("Helvetica", 10)
    c.drawString(30, y_position, "Converted JSON Data:")

    y_position -= 20  # Space between sections

    # Helper function to recursively handle nested JSON structures
    def draw_json(key, value, y_pos):
        nonlocal c
        if isinstance(value, dict):  # If it's a dictionary, recursively call the function
            c.drawString(30, y_pos, f"{key}: {{")
            y_pos -= 20
            for sub_key, sub_value in value.items():
                y_pos = draw_json(sub_key, sub_value, y_pos)
            c.drawString(30, y_pos, "}")
            y_pos -= 20
        elif isinstance(value, list):  # If it's a list, iterate through the items
            c.drawString(30, y_pos, f"{key}: [")
            y_pos -= 20
            for item in value:
                y_pos = draw_json("-", item, y_pos)  # Using '-' to denote list items
            c.drawString(30, y_pos, "]")
            y_pos -= 20
        else:  # If it's a basic value (string, number, etc.), just print it
            line = f"{key}: {str(value)}"
            c.drawString(30, y_pos, line)
            y_pos -= 20
        return y_pos

    # Start drawing the JSON structure
    for key, value in json_data.items():
        y_position = draw_json(key, value, y_position)
        if y_position <= 40:  # If we're too close to the bottom, add a new page
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = height - 40  # Reset position for the new page

    c.save()

# Streamlit app
def main():
    st.title("JSON to PDF Converter")
    st.write("Upload a JSON file to Convert to PDF.")

    # Drag-and-drop file uploader for JSON
    uploaded_file = st.file_uploader("Upload JSON file", type="json")
    
    if uploaded_file is not None:
        try:
            # Load JSON data
            json_data = json.load(uploaded_file)
            
            # Create a temporary directory to store the generated PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                pdf_path = temp_pdf.name
            
            # Convert the JSON data to PDF
            json_to_pdf(json_data, pdf_path)
            
            # Provide a download link for the PDF
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label=" 💾  Download PDF",
                    data=pdf_file,
                    file_name="converted_data.pdf",
                    mime="application/pdf"
                )

            # Clean up the temporary file
            os.remove(pdf_path)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Directly call the main function
main()
