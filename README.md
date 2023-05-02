# Barcode Analysis API for Smart Manufacturing
Barcode analysis is a crucial factor to consider in product packaging. Barcodes are present on most products, and it is essential to ensure that they are both accurate and readable. However, manually verifying the barcodes of numerous products is a time-consuming and costly task that is prone to errors. To overcome this challenge, computer vision systems can quickly and accurately verify barcodes, identifying any products with faulty codes and redirecting them accordingly. In this practice, we will demonstrate how to generate a barcode, extract its type and data and then wrap up its data extraction system into an API for further utilization.


# Project Walkthrough
 - Generate EAN13 barcode as png file using **barcode** python library.
 - Extract barcode data and type using **pyzbar** python library.
 - Build an API based on **flask** for barcode data and type extraction.

# Dependencies
```
Barcode
UUID
OPenCV
Numpy
Pyzbar
Requests
Json
Jsonpickle
Flask
```

# Dataset
For testing our system, we have used images from the internet, in particular manufactured products images such as bottles, snacks, boxes, cans...

![testing_images](https://user-images.githubusercontent.com/48753146/235614962-b477d354-9c3d-4540-83f2-5cd0053ce66d.PNG)

# Barcodes Generation
barcode is a python library used to create different standard types of barcodes. The library can generate SVG objects as well as PNG images. Python-barcode can generate the following types of barcodes:
 - EAN-8
 - EAN-13
 - EAN-14
 - UPC-A 
 - JAN
 - ISBN-10
 - ISBN-13
 
 ```
from barcode import EAN13                   # imported to create EAN13 barcodes
from barcode.writer import ImageWriter      # imported to save generated bar
import uuid                                 # imported to generate unique numbers, later used for barcode creation.

# Create Random and Unique number for our barcode
random_number = str(uuid.uuid1().int)[:14]
print(random_number)

# Create an EAN13 barcode
my_code = EAN13(random_number, writer=ImageWriter())

# Save the barcode as png image
my_code.save("barcode_1")
 
 ```
 
 ### Barcode Reading From the Generated Barcodes
 
 Example1
 ![test1](https://user-images.githubusercontent.com/48753146/235617759-0442beff-6777-40a3-a0f1-309b556a7968.PNG)
 
 Example2
 ![test2](https://user-images.githubusercontent.com/48753146/235618660-4a0f00e5-b12f-4bd5-9f7e-87766ba047dd.PNG)

# Test API
The API takes as input the product image containing the barcode, read it and output the result as a json response with 3 key pieces of information: barcode data, barcode type and request status.

![api_test](https://user-images.githubusercontent.com/48753146/235629296-6effb96c-d443-4cf5-90c8-8d366eb00b2a.PNG)


### API message codes
We have 3 messages codes:
 - 200: successful request
 - 404: no barcode data has been extracted
 - 403: wrong authentification key
 
 ![error_code](https://user-images.githubusercontent.com/48753146/235628641-270b0a12-e21e-4167-a329-5dd098f1e3b0.PNG)



# Improvment
 - Try different barcode readers libraries since Pyzbar does not support all barcode types. It was unable to work on certain products like `product20` from our dataset.
 
