#===
# This script looks at edge detection, specifically, Sobel
# and Canny edge detection
#
# Functions used:
# - cvtColor()
# - Sobel()
# - Canny()
#===
import cv2

# First, load an image
img = cv2.imread('../images/standard_test_images/baboon.png')
#img = cv2.imread('../images/tiger.jpg')

# Next, convert the image to grayscale with cvtColor()
# since color information is not needed to detect edges,
# and apply a Gaussian blur since it smooths out noise 
# for the derivatives
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(3,3),
                            sigmaX=0,sigmaY=0)

# Sobel Edge detection
sobelx = cv2.Sobel(src=img_blur,
                   ddepth=cv2.CV_64F, 
                   dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur,
                   ddepth=cv2.CV_64F, 
                   dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_blur,
                   ddepth=cv2.CV_64F, 
                   dx=1, dy=1, ksize=5)

# Canny Edge detection
edges = cv2.Canny(image=img_blur,
                  threshold1=100, 
                  threshold2=200)

# Display the images
cv2.imshow("Original",img)
cv2.imshow("Grayscale w/ blur",img_blur)
cv2.imshow("Sobel in x-direction",sobelx)
cv2.imshow("Sobel in y-direction",sobely)
cv2.imshow("Sobel in xy-direction",sobelxy)
cv2.imshow("Canny Edge detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# === Description ===
# Sobel edge detection works by convolution with
# the following kernels:
#   [-1 0 1]      [ 1  2  1]
#   [-2 0 2]      [ 0  0  0]
#   [-1 0 1]      [-1 -2 -1]
#  x-direction   y-direction
# It's essentially just enhancing intensity changes
# near edges. The dx and dy parameters indicate the
# spatial derivative and order (1=1st)
# 
# Canny edge detection is a 4-stage process:
# 1) Noise reduction - apply a Gaussian blur
# 2) Calculate intensity gradient - apply
#    Sobel kernels horizontally and vertically
#    and add in quadrature to get overall
#    gradient
# 3) Suppress false edges - if the magnitude
#    of the gradient of the current pixel is 
#    less than its neighbors, set it to 0
# 4) Hysteresis thresholding - restrict the 
#    gradient magnitude to fall within a 
#    upper and lower threshold