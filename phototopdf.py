import streamlit as st
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os

# Function to convert images to PDF
def images_to_pdf(images, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    page_width, page_height = letter

    # Define the gap for left and right margins
    margin_left_right = 50  # You can adjust this gap as per your requirement

    # Calculate the usable width after accounting for the margins
    usable_width = page_width - 2 * margin_left_right

    for img, img_name in images:
        img_width, img_height = img.size
        
        # Calculate the scaling factor to fit the image into the usable width
        scale_factor = min(usable_width / img_width, page_height / img_height)

        # If the image is smaller than the page (even after scaling), it won't be resized
        if scale_factor > 1:
            scale_factor = 1

        # Calculate new dimensions after applying the scale factor
        new_img_width = img_width * scale_factor
        new_img_height = img_height * scale_factor

        # Calculate position to center the image on the page with the left-right gap
        x_pos = (page_width - new_img_width) / 2  # Horizontal centering
        y_pos = (page_height - new_img_height) / 2  # Vertical centering

        # Save the image temporarily as PNG
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_img_file:
            temp_img_path = temp_img_file.name
            img.save(temp_img_path, format="PNG")
        
        # Draw the image on the page with the calculated size and position
        c.drawImage(temp_img_path, x_pos, y_pos, width=new_img_width, height=new_img_height)

        # Add the image name below the image
        name_position = y_pos - 20  # 20px space between image and name
        c.setFont("Helvetica", 12)
        c.drawString((page_width - len(img_name) * 6) / 2, name_position, img_name)  # Center the name

        # Add a new page after each image
        c.showPage()

        # Clean up temporary image file
        os.remove(temp_img_path)

    c.save()

# Streamlit app
def main():
    st.title("Images to PDF Converter")
    st.write("Select one or more image to convert to PDF, it will be patched with file name")

    # Multi-image uploader
    uploaded_files = st.file_uploader("Upload Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if uploaded_files:
        # Load the images and store their names
        images = []
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            img_name = uploaded_file.name
            images.append((img, img_name))  # Store image and name as a tuple

        # Create a temporary file to save the generated PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            pdf_path = temp_pdf.name
        
        # Convert the images to PDF
        images_to_pdf(images, pdf_path)

        # Provide a download button for the PDF
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label=" 💾 Download PDF",
                data=pdf_file,
                file_name="images_with_names_to_pdf.pdf",
                mime="application/pdf"
            )

        # Clean up the temporary PDF file
        os.remove(pdf_path)

# Directly call the main function
main()
