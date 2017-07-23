#-*- coding: utf-8 -*-

import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import vision

if len(sys.argv) < 2:
    print 'Usage: python {0} <img-name>'.format(sys.argv[0])
else:
    # Instantiates a client
    vision_client = vision.Client()

    # The name of the image file to annotate
    img_name = sys.argv[1]
    file_name = os.path.join(os.path.dirname(__file__), img_name)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(content=content)

    # Performs label detection on the image file
    #labels = image.detect_labels()
    texts = image.detect_text()
    i=0
    for text in texts:
        print text.description
        if i == 0:
            break
    '''
    print('Labels:')
    for label in labels:
        print(label.description)
    '''
