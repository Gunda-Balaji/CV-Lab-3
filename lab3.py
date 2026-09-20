import cv2
import matplotlib.pyplot as plt
import numpy as np
def average_filter(img,kernel_size):
    pad=kernel_size//2
    output=np.zeros_like(img)
    for i in range(pad,img.shape[0]-pad): 
        for j in range(pad,img.shape[1]-pad):
            window=img[i-pad:i+pad+1,j-pad:j+pad+1]
            output[i,j]=np.mean(window)
    return output
def show_comparison(original,blur3,blur5,blur7):
    plt.figure(figsize=(12,8))
    plt.subplot(2,2,1)
    plt.imshow(original,cmap='gray')
    plt.title("Original Grayscale Image")
    plt.axis('off')
    
    plt.subplot(2,2,2)
    plt.imshow(blur3,cmap='gray')
    plt.title("Average Filter(3*3)")
    plt.axis('off')

    plt.subplot(2,2,3)
    plt.imshow(blur5,cmap='gray')
    plt.title("Average Filter(5*5)")
    plt.axis('off')

    plt.subplot(2,2,4)
    plt.imshow(blur7,cmap='gray')
    plt.title("Average Filter(7*7)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
img=cv2.imread("Forest for Lab3.jpg",0)
if img is None:
  print("Error:Image not found.")
else:
  blur_3x3 = average_filter(img,3)
  blur_5x5 = average_filter(img,5)
  blur_7x7 = average_filter(img,7)
  show_comparison(img,blur_3x3,blur_5x5,blur_7x7)
               

    
