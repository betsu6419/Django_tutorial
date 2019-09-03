import numpy as np
from keras.models import load_model as load
from keras.layers import *
import cv2
from .utils import *
from sys import argv
import os
from main.settings import BASE_DIR
os.environ[ 'TF_CPP_MIN_LOG_LEVEL'] = '2'

"""
Keras should be 1.2.2 ver. !!!!
"""
def predict(path):
    #img_file_path = argv[1]
    img_file_path = path
    img = cv2.imread(img_file_path)
    img_array = process_image(img)

    model_path = os.path.join(BASE_DIR,"allergies/food_predict/model4b.10-0.68.hdf5")
    model = load(model_path)
    result = model.predict(img_array)

    index = result.argmax()
    confidence = result.max()

    food = num2food(index)
    print("predicted:", food)
    print("confidence:", confidence)

    return str(food),confidence
