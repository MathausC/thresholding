from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np

max_value = 255
max_type = 4
max_binary_value = 255


parser = argparse.ArgumentParser(description='Code for Basic Thresholding Operations tutorial.')
parser.add_argument('--input', help='Path to input image.', default='stuff.jpg')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

# Convert the image to Gray
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

pixelsValues = cv.split(src_gray)[1]

max_pixel_value = np.max(pixelsValues)

min_pixel_value = np.min(pixelsValues)

def get_thresholding_image(self, image, diference):
    pixelsValues = cv.split(image)[1]
    max_pixel_value = np.max(image)
    min_pixel_value = np.min(image)
    midle_point = (max_pixel_value + min_pixel_value)/2
    position_255 = []
    position_0 = []
    
    threshold(self, pixelsValues, midle_point, position_255, position_0)
    final_threshold = get_new_threshold(self, midle_point, pixelsValues, position_255, position_0, diference)
    do_threshold(self, pixelsValues, final_threshold, position_255, position_0)
    return pixelsValues

def threshold(self, pixelsValues, midle_point, position_255, position_0):
    for line in range(len(pixelsValues)):
        for column in range(len(pixelsValues[line])):
            if (pixelsValues[line][column] >= midle_point):
                position_255.append((line, column))
            else :
                position_0.append((line, column))

def get_mean(self, array):
    count_array = []
    for i in table:
        line = i[0]
        column = i[1]
        count_array.append(pixelsValues[line][column])
    return np.mean(count_array)

def get_new_threshold(self, last_threshold, pixelsValues, position_255, position_0, diference):

    mean_255 = get_mean(self, position_255)

    mean_0 = get_mean(self, position_0)

    new_threshold = (mean_0 + mean_255)/2

    if (abs(last_threshold - new_threshold) <= diference):
        self.threshold(self, pixelsValues, midle_point, position_255, position_0)
        new_threshold = self.get_new_threshold(self, new_threshold, pixelsValues, position_255, position_0, diference)

    return new_threshold
    
def do_threshold(self, pixelsValues, midle_point, position_255, position_0):
    for line in range(len(pixelsValues)):
        for column in range(len(pixelsValues[line])):
            if (pixelsValues[line][column] >= midle_point):
                pixelsValues[line][column] = 255
            else :
                pixelsValues[line][column] = 0

thresholding_image = get_thresholding_image(self, pixelsValues, 0.001)

print(thresholding_image)