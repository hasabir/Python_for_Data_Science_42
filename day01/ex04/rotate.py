from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# def rotate(image_path):
#     # print(ft_load(image_path))
#     img = Image.open(image_path)
#     width, height = img.size
#     left = (width - 400) // 2
#     top = (height - 400) // 2
#     right = (width + 400) // 2
#     bottom = (height + 400) // 2

#     img = img.crop((left, top, right, bottom))
#     img = img.convert('L')

#     img_array = np.array(img)

#     # img_array = np.transpose(img_array)
#     image_new_shape = img_array[:, :, np.newaxis].shape
    
#     print(f'New shape after slicing: {image_new_shape} or {img_array.shape}')
#     plt.imshow(img_array, cmap='gray')
#     print(img_array.reshape(image_new_shape)[0][1])
#     # plt.show()


# def main():
#     rotate('animal.jpeg')


# if __name__ == '__main__':
#     main()



a = [[1, 2, 3], [1, 1, 3]]

# Initialize b as an empty list
b = []

# Transpose a into b
b.append([a[0][0], a[1][0]])
b.append([a[0][1], a[1][1]])
b.append([a[0][2], a[1][2]])

print('a =', a)
print('b =', b)
