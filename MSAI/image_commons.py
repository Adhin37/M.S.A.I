"""
This module contains functions used to manipulate images in OpenCV and PIL's Image.
"""
import cv2
import numpy as np
from PIL import Image


def image_as_nparray(image):
    """
    Converts PIL's Image to numpy's array.
    :param image: PIL's Image object.
    :return: Numpy's array of the image.
    """
    return np.asarray(image)


def nparray_as_image(nparray, mode='RGB'):
    """
    Converts numpy's array of image to PIL's Image.
    :param nparray: Numpy's array of image.
    :param mode: Mode of the conversion. Defaults to 'RGB'.
    :return: PIL's Image containing the image.
    """
    return Image.fromarray(np.asarray(np.clip(nparray, 0, 255), dtype='uint8'), mode)


def load_image(source_path):
    """
    Loads RGB image and converts it to grayscale.
    :param source_path: Image's source path.
    :return: Image loaded from the path and converted to grayscale.
    """
    source_image = cv2.imread(source_path)
    return cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)


def draw_with_alpha(source_image, image_to_draw, coordinates):
    """
    Draws a partially transparent image over another image.
    :param source_image: Image to draw over.
    :param image_to_draw: Image to draw.
    :param coordinates: Coordinates to draw an image at. Tuple of x, y, width and height.
    """
    x, y, w, h = coordinates
    image_to_draw = image_to_draw.resize((h, w), Image.ANTIALIAS)
    image_array = image_as_nparray(image_to_draw)
    for c in range(0, 3):
        source_image[y:y + h, x:x + w, c] = image_array[:, :, c] * (image_array[:, :, 3] / 255.0) \
                                            + source_image[y:y + h, x:x + w, c] * (1.0 - image_array[:, :, 3] / 255.0)

def draw_rectangle(source_image,index,coordinates):
    """
    Draws a partially transparent image over another image.
    :param source_image: Image to draw over.
    :param image_to_draw: Image to draw.
    :param coordinates: Coordinates to draw an image at. Tuple of x, y, width and height.
    """
    x, y, w, h = coordinates
    cv2.rectangle(source_image, (x,y), (x+w,y+h), 255,2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if index == 1:
 	cv2.putText(source_image,'anger',(x+w/2,y-h/2), font, 1, (255,25,255), 2, cv2.LINE_AA)
    elif index == 2:
	cv2.putText(source_image,'disgust',(x+w/2,y-h/2), font, 1, (255,25,255), 2, cv2.LINE_AA)
    elif index == 3:
	cv2.putText(source_image,'happy',(x+w/2,y-h/2), font, 1, (255,25,255), 2, cv2.LINE_AA)
    elif index == 4:
	cv2.putText(source_image,'sadness',(x+w/2,y-h/2), font, 1, (255,25,255), 2, cv2.LINE_AA)
    elif index == 5:
	cv2.putText(source_image,'surprise',(x+w/2,y-h/2), font, 1, (255,25,255), 2, cv2.LINE_AA)
    else:
	cv2.putText(source_image,'neutral',(x+w/2,y-h/2), font, 1, (255,25,255), 2, cv2.LINE_AA)
    #cv2.putText(source_image,'exact',(x+w,y+h),255,2)
 
   
