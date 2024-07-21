from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoom(image_path):
    """
    Loads an image, prints its dimensions, number of channels,
    pixel content, and displays it with scales on the X and Y axes.

    Parameters:
    image_path (str): The path to the image file.
    """
    try:
        pixel_values, img = ft_load(image_path)
        print(pixel_values)
        width, height = img.size
        left = (width - 400) // 2
        top = (height - 400) // 2
        right = (width + 400) // 2
        bottom = (height + 400) // 2

        img = img.crop((left, top, right, bottom))
        img = img.convert('L')
        img_array = np.array(img)
        image_new_shape = img_array[:, :, np.newaxis].shape
        print(f"New shape after slicing: \
              {image_new_shape} or {img_array.shape}")
        plt.imshow(img_array, cmap='gray')
        print(img_array.reshape(image_new_shape))
        plt.show()
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")


def main():
    '''main function for to test zoom function'''
    zoom('animal.jpeg')
    # print(zoom.__doc__)


if __name__ == '__main__':
    main()
