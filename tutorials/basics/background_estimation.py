#===
# This script does a simply background estimation
# of a video by assigning each pixel to its
# median value (temporal median filtering), then
# this is used to mask the moving objects in the
# video
#
# Functions used:
# - set()
# - absdiff()
#===
import cv2
import numpy as np
from skimage import data, filters

# Open the video
cap = cv2.VideoCapture("../videos/traffic3.mp4")

# === Temporal median filter to get Background === 

# Randomly select some frames
num_frames = 50
frameIds   = (cap.get(cv2.CAP_PROP_FRAME_COUNT) * 
              np.random.uniform(size=num_frames))

# Store the frames in an array using set()
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)

# Display median frame
cv2.imshow('Median frame', medianFrame)
cv2.waitKey(0)

# === Mask each frame for moving objects === 

# Reset the frame number to 0
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Convert the background to grayscale
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)

# Loop over the frames
ret = True
while (ret):
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference of current
    # frame and the median frame
    diff = cv2.absdiff(frame, grayMedianFrame)

    # Apply a binary threshold
    th, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Display the frame
    cv2.imshow("Frame", diff)
    cv2.waitKey(20)

# Release the video object
cap.release()
cv2.destroyAllWindows()
