from load_image import ft_load
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#! load function for what


def ft_transpose(lst: np.array) -> np.array:
    result = []
    for i in range(lst.shape[1]):
        stock = [lst[j][i] for j in range(lst.shape[0])]
        result.append(stock)
    return np.array(result)


def rotate(image_path: str) -> None:
	img = Image.open(image_path)
	width, height = img.size
	left = (width - 400) // 2
	top = (height - 400) // 2
	right = (width + 400) // 2
	bottom = (height + 400) // 2

	img = img.crop((left, top, right, bottom))
	img = img.convert('L')

	img_array = np.array(img)

	# img_array = ft_transpose(img_array)
	image_new_shape = img_array[:, :, np.newaxis].shape
	
	print(f'The shape of the image is: {image_new_shape} or {img_array.shape}')
	print(img_array.reshape(image_new_shape))
	

	t_image = ft_transpose(img_array)
	print(f'New shape after Transpose is: {t_image.shape}')
	# print(t_image.reshape(t_image[:, :, np.newaxis].shape))
	print(t_image)
	
	plt.imshow(t_image, cmap='gray')
	plt.show()


def main():
	rotate('animal.jpeg')


if __name__ == '__main__':
	main()

