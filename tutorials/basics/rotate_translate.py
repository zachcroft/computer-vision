#===
# This script looks at how to rotate and translate
# images (i.e., affine transformations)
#
# Functions used:
# - getRotationMatrix2D()
# - warpAffine()
#===
import cv2
import numpy as np

# Load the image
img = cv2.imread("../images/ocean.png")

# Extract the width and height and use
# it to get the image center
height, width = img.shape[:2]
center = (width/2, height/2)

# === Rotation ===
# Create a rotation matrix with getRotationMatrix2D()
rotation_matrix = cv2.getRotationMatrix2D(center=center,
                                          angle=45,
                                          scale=1)

# Rotate the image using warpAffine()
rotated_img = cv2.warpAffine(src=img,
                             M=rotation_matrix,
                             dsize=(width,height))

# === Translation ===
# Define the translations for each direction
tx, ty = width/4, height/4

# Create the translation matrix
translation_matrix = np.array([[1, 0, tx],
                               [0, 1, ty]],
                               dtype=np.float32)

# Apply the translation matrix with warpAffine()
translated_img = cv2.warpAffine(src=img, 
                                M=translation_matrix,
                                dsize=(width,height))



# Display the images
cv2.imshow("Original", img)
cv2.imshow("Rotated image", rotated_img)
cv2.imshow("Translated image", translated_img)
cv2.waitKey()
cv2.destroyAllWindows()

# === Description ===
# 
# The rotation matrix is defined as
#      [cos(theta) -sin(theta)]
#  M = [sin(theta)  cos(theta)]
#
# The translation matrix is defined as
#      [1 0 tx]
#  M = [0 1 ty]
#
# These are affine transformations,
# meaning parallel lines in the original
# image will remain parallel in the 
# transformed image
