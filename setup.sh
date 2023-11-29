#!/bin/sh

# Download Tesseract
curl -L https://github.com/tesseract-ocr/tesseract/archive/4.1.1.tar.gz | tar xz
cd tesseract-4.1.1
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
# Go back to the root directory
cd ..
