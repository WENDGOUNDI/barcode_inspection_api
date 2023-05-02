from __future__ import print_function
import requests
import json
import cv2


url = "http://localhost:5000/barcode_data_extraction?key=@5\FDVakRB0a0Nv=PwMr"

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

# Reading the image
img = cv2.imread('./test_images/product20_barcode.jpg')

# encode image as png
_, img_encoded = cv2.imencode('.png', img)

# send http request with image and receive response
response = requests.post(url, data=img_encoded.tostring(), headers=headers)
print(response.text)