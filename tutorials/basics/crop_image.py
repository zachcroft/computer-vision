#===
# This script simply crops an image using basic cv2 functions
# Cropping is accomplished with array slicing
#===

import cv2
import numpy as np

# Read the image and print the dimensions
img = cv2.imread('../images/standard_test_images/baboon.png')
print(img.shape)
cv2.imshow("Original", img)

# Crop the image using array slicing
cropped_img = img[50:300,200:400]
cv2.imshow("Cropped", cropped_img)

# Save the image with imwrite()
#cv2.imwrite("cropped_baboon.png", cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()