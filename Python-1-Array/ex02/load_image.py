import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
        img_array = np.array(img)
        shape = img_array.shape
        print('The shape of image is:', shape)
        pixel_values = list(img.getdata())
        pixel_values = np.array(pixel_values).reshape(shape)
        return pixel_values

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def main():
    result = ft_load("landscape.jpg")
    if result is not None:
        print(result)


if __name__ == "__main__":
    main()
