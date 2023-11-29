import streamlit as st
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
import io

# Set the title of the app
st.title('PDF OCR App')

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert uploaded PDF to a list of images
    pages = convert_from_bytes(uploaded_file.read())

    # Loop through each page/image
    for i, page_image in enumerate(pages):
        st.write(f'Page {i + 1}')

        # Apply OCR to the image
        page_text = pytesseract.image_to_string(page_image)
        st.text_area("Extracted Text", page_text, height=250)
