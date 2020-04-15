# -*- coding: utf-8 -*-

import cv2
import numpy as np
import img_utils

line_spacing = 12
extend_point = 40
extra_padding = 8

def get_average_height(rects):
    line_count = len(rects)
    total_height = sum([rect[3] for rect in rects])
    return int(total_height / line_count)

def merge_rect(rect_one, rect_two):
    x1 , y1 , w1, h1 = rect_one
    x2 , y2 , w2, h2 = rect_two
    x = min(x1, x2)
    y = min(y1, y2)
    w = max(w1, w2)
    h = h1 + h2
    return ( x, y, w, h)

def enlarge(rect):
    x, y, w, h = rect
    # re_extend top and bottom, re_shrink left and right to match original contour
    # and add extra padding to ensure to cover line
    
    x += ( extend_point - extra_padding  )
    y -= ( line_spacing + extra_padding  )
    w -= ( (extend_point * 2) - ( extra_padding ) ) 
    h += ( line_spacing + extra_padding )
    return (x, y, w, h)

def get_lines(img):
    # binary = img_utils.invert(img)
    binary = cv2.bitwise_not(img)
    # binary = (255-img)
    width, height = binary.shape
    black = img_utils.black(width, height)
    #find contours   
    ctrs, hier = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contours to bounding Rectangle
    rects = [ cv2.boundingRect(ctr) for ctr in ctrs]
    # sorted by x coordinate
    rects = sorted(rects, key=lambda rect: rect[0])
    # remove rect with low height from list
    rects = [rect for rect in rects if rect[3] > 5 ]

    ###################################
    #### stage 1: merging character ###
    ###################################
    # draw rectangle on totally black image    
    for rect in rects:
        x, y, w, h = rect 
        # extend left and right of rectangle and shrink top and bottom
        x -= extend_point  
        y += line_spacing
        w += extend_point * 2
        h -= line_spacing
        cv2.rectangle(black,(x,y),( x + w , y + h ),(255,255,255), -1)

    # re_retrive contours from previous draw rectangle
    ctrs, hier = cv2.findContours(black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = [ cv2.boundingRect(ctr) for ctr in ctrs]

    ##################################################
    #### stage 2: drawing line box on blank image ####
    ##################################################
    black = img_utils.black(width, height)
    for rect in rects:
        x, y, w, h = rect
        cv2.rectangle(black,(x,y),( x + w , y + h ),(255,255,255), -1)

    ######################################################################
    #### stage 3: find and remove the lines which are separated from
    ### constant chracters line
    ######################################################################
    ctrs, hier = cv2.findContours(black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = [ cv2.boundingRect(ctr) for ctr in ctrs]
    rects = sorted(rects, key=lambda rect: rect[1])
    avg_height = get_average_height(rects)
    rects = [ rect for rect in rects if  avg_height < rect[3] * 2]

    black = img_utils.black(width, height)
    for rect in rects:
        x, y, w, h = rect 
        cv2.rectangle(black,(x,y),( x + w , y + h ),(255,255,255), -1)

    ctrs, hier = cv2.findContours(black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rects = [ cv2.boundingRect(ctr) for ctr in ctrs]
    rects = sorted(rects, key=lambda rect: rect[1])
    lines = len(rects)
    print('initial line counts:', lines)
    avg_height = get_average_height(rects)
    print('average_height: ', avg_height)

    ######################################################################
    #### stage 4: reshape bounding rect for line which are wrong ###
    ######################################################################

    height_of_upper_vowels_line = (int) (avg_height / 4.5) # estimate vowel height
    # constant base line may be separated from above or blow or both
    for _ in range(2):
        for i, rect in enumerate(rects):
            x, y, w, h = rect
            if  h + height_of_upper_vowels_line < avg_height:
                print('line witout upper vowel or lower vowel: height is ', h)
                previous_rect = rects[i-1]
                new_height = h + height_of_upper_vowels_line
                if y - ( new_height + line_spacing) > previous_rect[1]:
                    y -= height_of_upper_vowels_line
                h += height_of_upper_vowels_line
                print('fiexed line height is ', h)            
                # print('fixed rect: ', (x, y, w, h))
            rects[i]=(x,y, w, h)

    #re_enlarge bounding box to cover lines
    rects = [ enlarge(rect) for rect in rects]
   
    return rects