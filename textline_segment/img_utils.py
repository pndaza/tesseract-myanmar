# -*- coding: utf-8 -*-

import cv2
import numpy as np

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def clean(img):
    # apply adaptive threshold
    ret2,threshold = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #deskew
    clean = deskew(threshold)
    return clean

def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    print('angle', angle)
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def get_average_height(rects):
    line_count = len(rects)
    # print('line count before processing: ', line_count)
    total_height = sum([rect[3] for rect in rects])
    raw_height = int(total_height / line_count)
    return int(total_height / line_count)

def merge_rect(rect_one, rect_two):
    x1 , y1 , w1, h1 = rect_one
    x2 , y2 , w2, h2 = rect_two
    x = min(x1, x2)
    y = min(y1, y2)
    w = max(w1, w2)
    h = h1 + h2
    return ( x, y, w, h)

def invert(img):
    # apply medain blur to remove noise
    blur = cv2.medianBlur(img,5)
    # convert to black and white
    ret, invert = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV + + cv2.THRESH_OTSU)
    return invert

def black(width,height):
    return np.zeros((width,height), dtype = "uint8")

def get_bounded_box_image(img, rects):
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for rect in rects:
        x, y, w, h = rect
        cv2.rectangle(img,(x,y),( x + w , y + h ),(255,0,255), 1)

    return img

