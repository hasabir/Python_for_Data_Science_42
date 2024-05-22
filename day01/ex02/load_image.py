from PIL import Image


img = Image.open("landscape.jpg")
# # img.show()
px = img.load()
print(list(img.getpixel((0,0))))
# print(list())



import cv2

image = cv2.imread('landscape.jpg')

print('The shape of image is:',image.shape)
