from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def ft_transpose(lst: np.array) -> np.array:
    result = []
    for i in range(lst.shape[1]):
        stock = [lst[j][i] for j in range(lst.shape[0])]
        result.append(stock)
    return np.array(result)

def rotate(image_path: str) -> None:
    # Use ft_load instead of Image.open
    img_array = ft_load(image_path)
    
    # Crop the image to 400x400
    height, width = img_array.shape[:2]
    left = (width - 400) // 2
    top = (height - 400) // 2
    img_array = img_array[top:top+400, left:left+400]
    
    # Convert to grayscale if it's not already
    if len(img_array.shape) == 3:
        img_array = np.mean(img_array, axis=2).astype(np.uint8)
    
    # Print original shape
    print(f"The shape of image is: {img_array.shape}")
    print(img_array.reshape(img_array.shape + (1,)))
    
    # Transpose the image
    t_image = ft_transpose(img_array)
    
    # Print new shape and transposed array
    print(f"New shape after Transpose: {t_image.shape}")
    print(t_image)
    
    # Display the image
    plt.imshow(t_image, cmap='gray')
    plt.show()

def main():
    rotate('animal.jpeg')

if __name__ == '__main__':
    main()