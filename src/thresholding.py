from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
from PIL import Image as im

parser = argparse.ArgumentParser(description='Code for Basic Thresholding Operations tutorial.')
parser.add_argument('--input', help='Path to input image.', default='../images/digital.jpg')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

# Convert the image to Gray
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

def get_thresholding_image(image, diference):
    pixelsValues = cv.split(image)[0]
    max_pixel_value = np.max(image)
    min_pixel_value = np.min(image)
    midle_point = (max_pixel_value + min_pixel_value)/2
    position_255 = []
    position_0 = []
    
    separa_regioes(pixelsValues, midle_point, position_255, position_0)
    final_threshold = get_new_threshold(midle_point, pixelsValues, position_255, position_0, diference)
    do_threshold(pixelsValues, final_threshold, position_255, position_0)
    return pixelsValues

def separa_regioes(pixelsValues, midle_point, position_255, position_0):
    for line in range(len(pixelsValues)):
        for column in range(len(pixelsValues[line])):
            if (pixelsValues[line][column] >= midle_point):
                position_255.append((line, column))
            else :
                position_0.append((line, column))

def get_mean(table, pixelsValues):
    count_array = []
    for i in table:
        line = i[0]
        column = i[1]
        count_array.append(pixelsValues[line][column])
    return np.mean(count_array)

def get_new_threshold(last_threshold, pixelsValues, position_255, position_0, diference):

    mean_255 = get_mean(position_255, pixelsValues)

    mean_0 = get_mean(position_0, pixelsValues)

    new_threshold = (mean_0 + mean_255)/2

    if (abs(last_threshold - new_threshold) <= diference):
        separa_regioes(pixelsValues, new_threshold, position_255, position_0)
        new_threshold = get_new_threshold(new_threshold, pixelsValues, position_255, position_0, diference)

    return new_threshold
    
def do_threshold(pixelsValues, midle_point, position_255, position_0):
    for line in range(len(pixelsValues)):
        for column in range(len(pixelsValues[line])):
            if (pixelsValues[line][column] >= midle_point):
                pixelsValues[line][column] = 255
            else :
                pixelsValues[line][column] = 0

thresholding_image = get_thresholding_image(src_gray, 0.001)

print(thresholding_image)
data = im.fromarray(thresholding_image)
data.save('image_threshold.png')