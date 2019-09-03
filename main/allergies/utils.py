import numpy as np
import cv2
import os
from main.settings import BASE_DIR
def zscore(x, axis = None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd  = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd
    return zscore

"""
def class_dict():
    classes = {}
    f = open("classes.txt")
    for i, line in enumerate(f.readlines()):
      classes[line.replace("\n", "")] = i
    return classes
"""

def rev_class_dict():
    classes = {}
    path = os.path.join(BASE_DIR,"allergies/food_predict/classes.txt")
    f = open(path)
    for i, line in enumerate(f.readlines()):
      classes[i] = line.replace("\n", "")
    return classes

"""
def food2num(food):
    classes = class_dict()
    return classes[food]
"""

def num2food(num):
    classes = rev_class_dict()
    return classes[num]

def process_image(img_array):
    #img_arrayは画像をcv2.imread()で読み込んでnp.arrayにしたもの。
    img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (299,299))
    img = zscore(img)
    img = img.reshape(1,299,299,3)
    return img
