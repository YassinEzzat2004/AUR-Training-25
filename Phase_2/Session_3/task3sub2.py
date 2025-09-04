import numpy as np
import matplotlib.pyplot as plt
import cv2
# Take notice that OpenCV handles the image as a numpy array when opening it
img = cv2.imread("shapes.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
out = img.copy()
red_mask=((out[:,:,2]<=40)&(out[:,:,1]<=40)&(out[:,:,0]>=255-40))
blue_mask=((out[:,:,2]>=255-40)&(out[:,:,1]<=40)&(out[:,:,0]<=40))
black_mask=((out[:,:,0]<=40)&(out[:,:,1]<=40)&(out[:,:,2]<=40))

out[red_mask]=(0,0,255)
out[blue_mask]=(0,0,0)
out[black_mask]=(255,0,0)



fig, axes = plt.subplots(1, 2)
axes[0].imshow(img)
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(out)
axes[1].set_title('Processed Image')
axes[1].axis('off')
plt.show()