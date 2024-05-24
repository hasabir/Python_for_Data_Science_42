from PIL import Image
import numpy
import cv2



def ft_load(path: str) -> numpy.array:
	img = Image.open(path)
	image = cv2.imread(path)

	print('The shape of image is:',image.shape)

	# px = img.load()
	# width, height = img.size
	pixel_values = list(img.getdata())
	pixel_values = numpy.array(pixel_values).reshape(image.shape)
	return pixel_values
	

def main():
	print(ft_load("landscape.jpg"))



if __name__ == "__main__":
	main()
# print(list(img.getpixel((2,0))))
# print(list())




