# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pytesseract

def get_text(rect, image, avg_height):
    x, y, w, h = rect
    # Getting ROI
    roi = image[y:y+h, x:x+w]
    bordersize = 10
    # add white padding to line image
    # if there is no padding around text, ocr error rate are high
    line_img = cv2.copyMakeBorder(
        roi,
        top=bordersize,
        bottom=bordersize,
        left=bordersize,
        right=bordersize,
        borderType=cv2.BORDER_CONSTANT,
        value=[255, 255, 255]
    )

    psm_mode = 7
    if ( h  + (h/2)  > avg_height * 2 ):
        psm_mode = 6

    config_str = '--psm ' + str(psm_mode) + ' --dpi 100'
    text = pytesseract.image_to_string(line_img, lang='mya', config=config_str)

    return text
