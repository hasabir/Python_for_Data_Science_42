from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_transpose(lst: np.array) -> np.array:
    """ Returns an array with axes transposed.

    Keyword arguments:
    lst -- list of ints
    Return:
    `lst` with its axes permuted. A view is returned whenever possible.
    """

    result = []
    for i in range(lst.shape[1]):
        stock = [lst[j][i] for j in range(lst.shape[0])]
        result.append(stock)
    return np.array(result)


def rotate(image_path: str) -> None:
    """
    Loads an image, crops it,
    transposes it, and displays it.

    Parameters:
    image_path (str): Path to the image file.
    """

    try:
        pixel_values, img = ft_load(image_path)

        # Crop the image to a 400x400 square centered
        width, height = img.size
        left = (width - 400) // 2
        top = (height - 400) // 2
        right = (width + 400) // 2
        bottom = (height + 400) // 2
        img = img.crop((left, top, right, bottom))

        img = img.convert('L')
        img_array = np.array(img)
        image_new_shape = img_array[:, :, np.newaxis].shape
        print(f'The shape of the image is:\
              {image_new_shape} or {img_array.shape}')
        print(img_array.reshape(image_new_shape))

        # Transpose the image array
        t_image = ft_transpose(img_array)
        print(f'New shape after transpose is: {t_image.shape}')
        print(t_image)

        # Display the transposed image
        plt.imshow(t_image, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    rotate('animal.jpeg')


if __name__ == '__main__':
    main()
