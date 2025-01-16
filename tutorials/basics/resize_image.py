#===
# This script simply resizes an image using basic cv2 functions
#
# Functions used:
# - imread()
# - imshow()
# - waitKey()
# - resize()
# - destroyAllWindows()
#===
import cv2
import numpy as np

# Read and display an image using imread() and imshow().
# The image will automatically close after imshow(), so
# the waitKey() function is needed.
image = cv2.imread('../images/standard_test_images/baboon.png')
cv2.imshow('Original image', image)
#cv2.waitKey()

# Downscale the image to a specified resolution using the
# resize() function and linear interpolation keyword
down_width  = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Downscaled image',resized_down)
#cv2.waitKey()

# Downscale the image to a specified resolution using the
# resize() function and linear interpolation keyword
up_width  = 800
up_height = 700
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Upscaled image',resized_up)
cv2.waitKey()

cv2.destroyAllWindows()