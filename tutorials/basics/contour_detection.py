#===
# This script demonstrates contour detection
#
# Functions used:
# - findContours()
# - copy()
# - drawContours()
# - split()
#===
import cv2

# === Grayscale version ===

# Read the image as grayscale
img = cv2.imread("../images/cats.jpg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
thresh    = 230
max_value = 255
ret, dst = cv2.threshold(img_gray, thresh, max_value, 
                        cv2.THRESH_BINARY)

# Find and draw contours using findContours()
#  - mode determines the type of contours
#  - method determines the contour retrieval 
#    algorithm
contours, hierarchy = cv2.findContours(image=dst, 
                                       mode=cv2.RETR_TREE,
                                       method=cv2.CHAIN_APPROX_NONE)

# Draw the contours
img_copy = img.copy()
cv2.drawContours(image=img_copy, 
                 contours=contours, 
                 contourIdx=-1,
                 color=(255,0,0),
                 thickness=2,
                 lineType=cv2.LINE_AA)

cv2.imshow("Original",img)
cv2.imshow("Grayscale",img_gray)
cv2.imshow("Binary threshold",dst)
cv2.imshow('None approximation', img_copy)
cv2.waitKey()
cv2.destroyAllWindows()

# === Color channels === 

# Split the image into RGB color channels
blue, green, red = cv2.split(img)

# Find contours for each color channel
contours_b, hierarchy_b = cv2.findContours(image=blue, 
                                           mode=cv2.RETR_TREE,
                                           method=cv2.CHAIN_APPROX_NONE)

contours_g, hierarchy_g = cv2.findContours(image=green, 
                                           mode=cv2.RETR_TREE,
                                           method=cv2.CHAIN_APPROX_NONE)

contours_r, hierarchy_r = cv2.findContours(image=red, 
                                           mode=cv2.RETR_TREE,
                                           method=cv2.CHAIN_APPROX_NONE)

img_contour_b = img.copy()
img_contour_g = img.copy()
img_contour_r = img.copy()

# Draw contours
cv2.drawContours(image=img_contour_b, 
                 contours=contours_b, 
                 contourIdx=-1,
                 color=(255,0,0),
                 thickness=2,
                 lineType=cv2.LINE_AA)

cv2.drawContours(image=img_contour_g, 
                 contours=contours_r, 
                 contourIdx=-1,
                 color=(255,0,0),
                 thickness=2,
                 lineType=cv2.LINE_AA)

cv2.drawContours(image=img_contour_r, 
                 contours=contours_g, 
                 contourIdx=-1,
                 color=(255,0,0),
                 thickness=2,
                 lineType=cv2.LINE_AA)

cv2.imshow('Contour detection using blue channels only', 
           img_contour_b)
cv2.imshow('Contour detection using green channels only', 
           img_contour_g)
cv2.imshow('Contour detection using red channels only', 
           img_contour_r)

cv2.waitKey()
cv2.destroyAllWindows()

# === CHAIN_APPROX_SIMPLE contour algorithm ===
# Description: compresses horizontal, vertical, 
#   and diagonal segments long the contour, so
#   it uses less memory
# Find the contours
contours, hierarchy = cv2.findContours(image=dst, 
                                       mode=cv2.RETR_TREE,
                                       method=cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours
img_copy = img.copy()
cv2.drawContours(image=img_copy, 
                 contours=contours, 
                 contourIdx=-1,
                 color=(255,0,0),
                 thickness=2,
                 lineType=cv2.LINE_AA)

cv2.imshow('Simple approximation', img_copy)

cv2.waitKey()
cv2.destroyAllWindows()