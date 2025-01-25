#===
# This script uses your webcam to take pictures
# continuously given a framerate
#===
import cv2

# Create a video capture object
webcam = cv2.VideoCapture(0)

# Choose a framerate
fps    = 60
period = int(1000 / fps)

ret = True
while ret:
    # Capture a frame
    ret, frame = webcam.read()

    # Display the frame
    cv2.imshow("Webcam capture", frame)
    cv2.waitKey(period)

# Release the object
webcam.release()