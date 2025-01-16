#===
# This script defines a kernel for performing convolution
# to create various image filtering effects
#
# Functions used:
# - filter2D()
# - blur()
# - GaussianBlur()
# - medianBlur()
# - bilateralFilter()
#===
import cv2
import numpy as np

# === DEFINE KERNEL FUNCTIONS ===
def apply_kernel_identity(img):
    # Define the identity kernel w/ a numpy array
    kernel_id = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]])
    
    # Apply the filter with the filter2D() function
    # ddepth controls image depth, -1 means the output
    # has the same depth as the input
    img_id = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_id)

    return img_id

def apply_kernel_blur(img):
    # Define a uniform matrix for blurring
    kernel_blur = np.ones((5,5), np.float32) /25
    
    # Apply the filter with the filter2D() function
    img_id = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_blur)

    return img_id

def apply_kernel_blur(img):
    # Define a uniform matrix for blurring
    kernel_blur = np.ones((5,5), np.float32) /20
    
    # Apply the filter with the filter2D() function
    img_id = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_blur)

    return img_id

def apply_kernel_sharpen(img):
    # Define a uniform matrix for sharpening
    kernel_sharpen  = np.array([[0, -1, 0],
                                [-1, 5, -1],
                                [0, -1, 0]])
    
    # Apply the filter with the filter2D() function
    img_id = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_sharpen)

    return img_id


# === MAIN CODE ===
# Read the image, showing an error message if it doesn't exist
img = cv2.imread('../images/standard_test_images/baboon.png')
if img is None:
    print('Could not read image')
cv2.imshow("Original", img)

# Apply custom filters
img_id      = apply_kernel_identity(img)
img_blur    = apply_kernel_blur(img)
img_sharpen = apply_kernel_sharpen(img)

# Note: opencv has a built-in blur() function
# It takes ksize as a parameter for the kernel
# This function seems to normalize the image so
# there is no brightness change
img_cv_blur = cv2.blur(src=img, ksize = (5,5))

# OpenCV has a built-in GaussianBlur() function
# It needs the std. dev. for each direction sigma
img_cv_gauss = cv2.GaussianBlur(src=img, ksize=(5,5),
                                sigmaX=0, sigmaY=0)

# OpenCV has a built-in medianBlur()
img_cv_med = cv2.medianBlur(src=img, ksize=5)

# OpenCV has a built-in bilateralFilter() function
# A bilateral filter considers differences in pixel
# intensities to avoid blurring edges.
# The parameter d is the diameter of the neighborhood.
# sigmaColor defines the tolerance for px intensity,
#  i.e., the Gaussian of 1D color distribution
# sigmaSpace defines the spatial std. dev 
img_cv_bilat = cv2.bilateralFilter(src=img, 
                                   d=9, 
                                   sigmaColor=75, 
                                   sigmaSpace=75)


# Display the filtered images
cv2.imshow("Identity kernel", img_id)
cv2.imshow("Blur filter", img_blur)
cv2.imshow("OpenCV blur()", img_cv_blur)
cv2.imshow("OpenCV GaussianBlur()", img_cv_gauss)
cv2.imshow("OpenCV medianBlur()", img_cv_med)
cv2.imshow("Sharpening filter", img_sharpen)
cv2.imshow("OpenCV bilateralFilter()", img_cv_bilat)
cv2.waitKey()
cv2.destroyAllWindows()