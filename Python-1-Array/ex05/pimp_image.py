from matplotlib import pyplot as plt
from numpy import array
import numpy as np


from load_image import ft_load


def ft_invert(array) -> array:
    ...



def ft_red(array) -> array:
    img = array[1]
    img = np.array(img)
    red_component=img.copy()
    red_component[:,:,1:3] *= 0
    plt.imshow(red_component)
    plt.show()

def ft_green(array) -> array:
    img = array[1]
    img = np.array(img)
    green_component=img.copy()
    green_component[::,::,2]=0
    green_component[::,::,0]=0
    
    plt.imshow(green_component)
    plt.show()

def ft_blue(array) -> array:
    img = array[1]
    img = np.array(img)
    blue_component=img.copy()
    blue_component[::,::,1]=0
    blue_component[::,::,0]=0
    
    plt.imshow(blue_component)
    plt.show()

def ft_grey(array) -> array:
    img = array[1]
    img = np.array(img)
    green_component=img.copy()
    hi = green_component
    hi = green_component[::,::,1]
    # green_component[::,::,0]=0
    
    plt.imshow(hi, cmap='gray')
    plt.show()

    # img = Image.open(path)



def main():
    array = ft_load("landscape.jpg")

    # ft_invert(array)
    # ft_red(array)
    # ft_green(array)
    ft_blue(array)
    ft_grey(array)

    img = array[1]
    img = np.array(img)
    # plt.imshow(img_array)
    # plt.show()
    
    blue_component=img.copy()
    blue_component[::,::,0:2]=0

    green_component=img.copy()
    green_component[::,::,2]=0
    green_component[::,::,0]=0

    # fig,ax=plt.subplots(1,3,figsize=(15,7))
    # i=0
    # for _ in (red_component,green_component,blue_component):
    #     ax[i].imshow(_)
    #     ax[i].axis('off')
    #     i+=1
    # plt.show()

if __name__ == '__main__':
    main()



    