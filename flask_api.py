from flask import Flask, request, Response, jsonify
import jsonpickle
import numpy as np
import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

AUTHENTICATION_KEY = "@5\FDVakRB0a0Nv=PwMr"

# Define a function to extract barcode information
def data_extraction(barcode_image):

    # Decode the barcode image
    detectedBarcodes = decode(barcode_image)

    # If not detected then print the info message
    if not detectedBarcodes:
        resp_message = { "Status": "Barcode Data Not Detected or is either blank or corrupted",
                        "Barcode Data": None,
                        "Barcode Type": None }

        return jsonify(response=resp_message), 404
    else:

        # Loop through all the detected barcodes in our image
        for barcode in detectedBarcodes:
            
            if barcode.data!="":
            
                # Convert barcode data from bytes to string
                var_barcode_data = barcode.data.decode("utf-8") 

            # Return the barcode data and type
            resp_message = { "Status": "Data Extracted",
                        "Barcode Data": var_barcode_data,
                        "Barcode Type": barcode.type }
            
            return jsonify(response=resp_message), 200



@app.route('/barcode_data_extraction', methods=['POST'])
def main():

    key = request.args.get('key', None)
    if key and key == AUTHENTICATION_KEY:

        r = request
        # convert string of image data to uint8
        nparr = np.fromstring(r.data, np.uint8)

        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img.shape

        # do some fancy processing here....
        data_extraction(img)

        # Extract barcode information through our define function
        response = data_extraction(img)

        return response
    else:
        resp_message = { "Status": "Invalid Authentification Key",
                        "Barcode Data": None,
                        "Barcode Type": None }
        return jsonify(response=resp_message), 403



# start flask app, we automatic debug
if __name__ == "__main__":
    app.run(debug=True)