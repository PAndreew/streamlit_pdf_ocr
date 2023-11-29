# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
