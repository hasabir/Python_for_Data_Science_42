import numpy as np
from PIL import Image


def ft_load(path: str):
    """
    Loads an image and prints its shape.

    Parameters:
    path (str): Path to the image file.

    Returns:
    tuple: A tuple containing:
        - numpy.ndarray: Pixel values of the loaded image.
        - PIL.Image.Image: The image object.

    Raises:
    FileNotFoundError: If the image file is not found.
    """

    try:
        img = Image.open(path)
        img_array = np.array(img)
        shape = img_array.shape
        print('The shape of image is:', shape)
        pixel_values = list(img.getdata())
        pixel_values = np.array(pixel_values).reshape(shape)
        return pixel_values, img

    except FileNotFoundError:
        raise FileNotFoundError("File Not found")
