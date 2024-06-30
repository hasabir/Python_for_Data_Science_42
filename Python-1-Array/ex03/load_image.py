from PIL import Image
import numpy
import cv2


def ft_load(path: str) -> numpy.array:
    img = Image.open(path)
    image = cv2.imread(path)
    print('The shape of image is:', image.shape)
    pixel_values = list(img.getdata())
    pixel_values = numpy.array(pixel_values).reshape(image.shape)
    return pixel_values
