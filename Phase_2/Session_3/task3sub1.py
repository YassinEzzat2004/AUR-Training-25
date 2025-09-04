import numpy as np
import cv2 
import matplotlib.pyplot as plt

def convolve(image,kernel):
    img_h,img_w=image.shape
    kernel_h,kernel_w=kernel.shape
    if (kernel_h %2) !=0:
        pad_h=kernel_h//2
        pad_w=kernel_w//2
        padded_img=np.pad(image,((kernel_h,kernel_h),(kernel_w,kernel_w)))
        output=np.empty((img_h-kernel_h+2*pad_h+1,img_w-kernel_w+2*pad_w+1),dtype=float)
        for i in range(img_h):
            for j in range(img_w):
                matrix=padded_img[i:i+kernel_h,j:j+kernel_w]
                output[i,j]=np.sum(matrix * kernel)
        return output
    else:
        return 'kernel shape must be odd'


img = cv2.imread('image.jpeg', cv2.IMREAD_GRAYSCALE)
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')
axes[0, 1].imshow(convolve(img, np.ones((5, 5)) / 25), cmap='gray')
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')
axes[1, 0].imshow(convolve(img, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])),
cmap='gray')
axes[1, 0].set_title('Horizontal Sobel Filter')
axes[1, 0].axis('off')
axes[1, 1].imshow(convolve(img, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])),
cmap='gray')
axes[1, 1].set_title('Vertical Sobel Filter')
axes[1, 1].axis('off')
plt.show()