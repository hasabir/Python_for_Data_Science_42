from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def zoom(image_path):
    print(ft_load(image_path))
    img = Image.open(image_path)
    width, height = img.size
    left = (width - 400) // 2
    top = (height - 400) // 2
    right = (width + 400) // 2
    bottom = (height + 400) // 2

    img = img.crop((left, top, right, bottom))
    img = img.convert('L')

    img_array = np.array(img)

    image_new_shape = img_array[:, :, np.newaxis].shape
    print(f'New shape after slicing: {image_new_shape} or {img_array.shape}')
    plt.imshow(img_array, cmap='gray')
    print(img_array.reshape(image_new_shape))
    plt.show()


def main():
    zoom('animal.jpeg')


if __name__ == '__main__':
    main()
