import numpy as np
import cv2 as cv2


def ft_load(path: str) -> np.array:
    try:

        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(f"Unable to load image: {path}")
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(f"The shape of image is: {image_rgb.shape}")
        return image_rgb

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def main():
    result = ft_load("landscape.jpg")
    if result is not None:
        print(result)


if __name__ == "__main__":
    main()
