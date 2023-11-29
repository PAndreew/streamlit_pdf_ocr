import streamlit as st
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import io
import tempfile

# Set the title of the app
st.title('PDF OCR App')

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmpfile:
        tmpfile.write(uploaded_file.getvalue())
        pdf_path = tmpfile.name

    # Convert PDF to a list of images
    pages = convert_from_path(pdf_path, 500)

    # Loop through each page/image
    for i, page_image in enumerate(pages):
        st.write(f'Page {i+1}')

        # Convert PIL Image to bytes
        with io.BytesIO() as output:
            page_image.save(output, format="JPEG")
            page_image_bytes = output.getvalue()

        # Apply OCR to the image
        page_text = pytesseract.image_to_string(Image.open(io.BytesIO(page_image_bytes)))
        st.text_area("Extracted Text", page_text, height=250)
