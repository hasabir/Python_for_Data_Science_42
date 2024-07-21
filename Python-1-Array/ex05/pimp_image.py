from matplotlib import pyplot as plt
from numpy import array
from load_image import ft_load
import numpy as np

def ft_invert(array) -> array:
    """Inverts the color of the image received."""

    img = np.array(array[1])
    inverted_img = 255 - img
    return inverted_img


def ft_red(array) -> array:
    """Apply Red filter of the image received."""

    img = np.array(array[1])
    img[:, :, 1:3] *= 0
    return img


def ft_green(array) -> array:
    """Apply Green filter of the image received."""

    img = np.array(array[1])
    img[::, ::, ::2] = 0
    return img


def ft_blue(array) -> array:
    """Apply Blue filter of the image received."""

    img = np.array(array[1])
    img[::, ::, 0:2] = 0
    ft_blue.__name__ = "blue"
    return img


def ft_grey(array) -> array:
    """Apply Grey filter of the image received."""

    img = np.array(array[1])
    gray_component = img[::, ::, 1]
    return gray_component


def main():
    '''main function for testing'''
    array = ft_load("landscape.jpg")
    print(array[0])
    figures = {
        "Original": np.array(array[1])[::, ::],
        "Invert": ft_invert(array),
        'Red': ft_red(array),
        'Green': ft_green(array),
        'Blue': ft_blue(array),
        'Grey': ft_grey(array)
    }

    fig, ax = plt.subplots(3, 2, figsize=(10, 7))

    for i, (figure_name, img_data) in enumerate(figures.items()):
        row = i // 2
        col = i % 2
        if figure_name == 'Grey':
            ax[row, col].imshow(img_data, cmap='gray')
        else:
            ax[row, col].imshow(img_data)
        ax[row, col].axis('off')
        ax[row, col].text(0.5, -0.1, f"Figure VIII.{i}: {figure_name}",
                          ha='center', va='center',
                          transform=ax[row, col].transAxes)

    plt.tight_layout()
    plt.show()

    print(ft_invert.__doc__)


if __name__ == '__main__':
    main()
