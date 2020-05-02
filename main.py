import os

import cv2 
import pytesseract

import tempfile

from pdf2image import convert_from_path, convert_from_bytes

from PIL import Image

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('test.pdf')

w, h = images[0].size
                   
images[0].crop((29, 90, 1480, 220)).save("test.jpg", "JPEG")

print('converting PDF to image')

img = cv2.imread('test.jpg')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
output = pytesseract.image_to_string(img, config=custom_config)

os.rename("test.pdf", output +".pdf" )

#TODO remove remove Comment
if os.path.exists("test.jpg"): 
  print("remove temporay file")   
  os.remove("test.jpg")
else:
  print("The file does not exist")