import streamlit as st
import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
import io

# Set the title of the app
st.title('PDF OCR App')

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Read the PDF file
    reader = PdfReader(uploaded_file)
    num_pages = reader.getNumPages()

    # Loop through each page
    for page in range(num_pages):
        st.write(f'Page {page+1}')
        page_obj = reader.getPage(page)

        # Extract text from page (you can also convert to image and use OCR)
        page_text = page_obj.extractText()
        st.text_area("Extracted Text", page_text, height=250)
