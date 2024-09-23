import cv2
import numpy as np

def load_image(image_path, grayscale=False):
    if grayscale:
        return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return cv2.imread(image_path)

def split_channels(image):
    B, G, R = cv2.split(image)
    return R, G, B

def merge_channels(R, G, B):
    return cv2.merge([R, G, B])

def save_image(image, output_path):
    cv2.imwrite(output_path, image)
