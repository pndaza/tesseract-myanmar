# -*- coding: utf-8 -*-

import cv2
import argparse
import os
import ocr
import img_utils
import line_segment

RESIZED_HEIGHT = 2500

def do_OCR(folder_path, mode):

    ext = ( 'jpg', 'jpeg', 'png', 'tif', 'tiff')
    for img_file in os.listdir(folder_path):
        if img_file.endswith(ext):
            img_basename = os.path.splitext(img_file)[0]
            print('\n')
            print('#################################')
            print('### processing:', img_file )
            print('#################################')
            print('\n')

            img = cv2.imread(os.path.join(folder_path,img_file), 0)
            img = img_utils.resize(img, height=RESIZED_HEIGHT)
            img = img_utils.clean(img)
            height, width = img.shape
            # invert = img_utils.invert(img)           
            lines = line_segment.get_lines(img)
            print('founded lines: ', len(lines))
            # max_width will be use as paragraph analyzer
            longest_line = (sorted(lines, key=lambda line: line[2]))[-1]
            max_x = longest_line[0] + longest_line[2]
            avg_height = (int) (sum([line[3] for line in lines]) / len(lines))

            if mode != 1:
                print('Processing OCR ... ')
                texts = ''
                paragraph_decider = 50
                for i, rect in enumerate(lines):
                    x = rect[0] + rect[2]
                    text_line = ocr.get_text(rect, img, avg_height)
                    if text_line:
                        texts += text_line.strip()
                        if   x + paragraph_decider < max_x:
                            texts += '\n'

                # save ocr text to file
                textfile = os.path.join(folder_path, img_basename + '.txt' )
                print('saved to: ', textfile)
                with open(textfile, 'w', encoding='utf-8') as out:
                    out.write(texts + '\n\n')

            
            if mode == 1 or mode == 2:
                print('saving bounded box image...')
                path = os.path.join( folder_path, 'debug')
                if not os.path.exists(path):
                    os.makedirs(path)
                debug_file = os.path.join(path, img_file)
                debug_img = img_utils.get_bounded_box_image(img, lines)
                cv2.imwrite(debug_file, debug_img)

if __name__ == "__main__":

    ap = argparse.ArgumentParser(description='textline segmentation and do ocr on these lines')
    ap.add_argument("-i", "--input", type=str, help='input image folder')
    ap.add_argument("-m", "--mode", type=int, nargs='?', const=0, default=0, help=' 0: OCR. 1: only save bounded image 2: OCR + save bounded image. ')
    args = ap.parse_args()
    if(args.input == None):
        print('usage: python main.py --input path_to_image_folder')
        print('usage: python main.py --input path_to_image_folder --mode 1')
        print('\tmode 0: ocr only')
        print('\tmode 1: save bounded box image only')
        print('\tmode 2: ocr + save bounded box image')
    else:
        do_OCR(args.input, args.mode)
