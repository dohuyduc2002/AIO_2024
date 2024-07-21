import cv2 # type: ignore
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir('/Users/microwave/AIO_2024/Module_2/Week2/Image_data')

bg1_image = cv2.imread('GreenBackground.png',1)
bg1_image = cv2.resize(bg1_image,(678,381))

ob_image = cv2.imread('Object.png',1)
ob_image = cv2.resize(ob_image,(678,381))

bg2_image = cv2.imread('NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image,(678,381))

def compute_difference(bg_img, input_img):
    return cv2.absdiff(bg_img, input_img)

difference_single_channel = compute_difference(bg1_image,ob_image)


def compute_binary_mask(difference_single_channel):
    _, binary_mask = cv2.threshold(difference_single_channel, 30, 255, cv2.THRESH_BINARY)
    return binary_mask

binary_mask = compute_binary_mask(difference_single_channel)


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output

replaced = replace_background(bg1_image,bg2_image,ob_image)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(cv2.cvtColor(ob_image, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Object Image')
ax[0].axis('off')

ax[1].imshow(cv2.cvtColor(replaced, cv2.COLOR_BGR2RGB))
ax[1].set_title('Image after Background Replacement and Adding Object')
ax[1].axis('off')

plt.show()
