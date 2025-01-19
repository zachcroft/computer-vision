#===
# This script looks at how to threshold an image
#
# Functions used:
# - threshold()
#===
import cv2

# Read the image as a grayscale image
src = cv2.imread("../images/standard_test_images/baboon.png",
                 cv2.IMREAD_GRAYSCALE)

# Apply a binary threshold (i.e., values below
# the threshold are set to min_value and values 
# above are set to max_value) using threshold(),
# which returns a tuple of (bool, image)
thresh    = 127
max_value = 255
ret, dst1 = cv2.threshold(src, thresh, max_value, 
                          cv2.THRESH_BINARY)

# Apply an inverse binary threshold (i.e., values 
# below the threshold are set to max_value and
# values above are set to min_value) 
thresh    = 127
max_value = 255
ret, dst2 = cv2.threshold(src, thresh, max_value, 
                          cv2.THRESH_BINARY_INV)

# Apply a truncate threshold (i.e., values 
# above the threshold are set to the threshold
# and values below are unchanged) 
thresh    = 127
ret, dst3 = cv2.threshold(src, thresh, max_value,
                          cv2.THRESH_TRUNC)

# Apply a zeroing threshold (i.e., values 
# above the threshold are unchanged and 
# values below are set to zero) 
thresh    = 127
ret, dst4 = cv2.threshold(src, thresh, max_value,
                          cv2.THRESH_TOZERO)

# Apply an inverted zeroing threshold (i.e., 
# values above the threshold are set to zero
# and values below are unchanged) 
thresh    = 127
ret, dst5 = cv2.threshold(src, thresh, max_value,
                          cv2.THRESH_TOZERO_INV)

cv2.imshow("Original", src)
cv2.imshow("Binary threshold", dst1)
cv2.imshow("Inverse binary threshold", dst2)
cv2.imshow("Truncate threshold", dst3)
cv2.imshow("Threshold to zero", dst4)
cv2.imshow("Inverse threshold to zero", dst5)
cv2.waitKey()
cv2.destroyAllWindows()