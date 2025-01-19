#===
# This script looks at how to read and write video files
#
# Functions used:
# - VideoCapture()
# - isOpened()
# - get()
# - read()
# - ord()
# - VideoWriter()
# - write()
# - release()
#===
import cv2

# === Reading a video ===

# Read the video using VideoCapture() to create
# a video capture object
vid_capture = cv2.VideoCapture('../videos/roundhay_garden.mp4')

if (vid_capture.isOpened() == False):
    print("Error opening file")
else:
    # Use get() to get metadata; the value
    # 5 specifies we should get the framerate
    fps = vid_capture.get(5)
    print("Frames per sec: ", fps, 'FPS')

    # Use get() to get metadata; the value
    # 7 specifies we should get the frame count
    frame_count = vid_capture.get(7)
    print("Frames count: ", frame_count)

while(vid_capture.isOpened()):
    # Use .read() to return a tuple (bool, frame), where
    # the bool is whether a frame exists
    ret, frame = vid_capture.read()
    
    if ret == True:
        # Display the frame
        cv2.imshow('Frame',frame)

        # Play the video with 20 ms between frames
        # but quit if a certain key (q) is pressed
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
    else:
        break

# Release the video capture object and 
# close the window
vid_capture.release()
cv2.destroyAllWindows()


# === Writing a video ===

# Read the video into a VideoCapture() object
vid_capture = cv2.VideoCapture('../videos/roundhay_garden.mp4')

# Get the frame width and height using get() 
# with parameters 3 and 4
frame_width  = int(vid_capture.get(3)) 
frame_height = int(vid_capture.get(4)) 
frame_size   = (frame_width, frame_height)
fps          = 20


# Create a VideoWriter() object for writing AVI
output = cv2.VideoWriter('../videos/test_out_AVI.avi',
                         cv2.VideoWriter_fourcc('M','J','P','G'), 
                         20, frame_size)

# Create a VideoWriter() object for writing MP4
#output = cv2.VideoWriter('../videos/test_out_MP4.mp4', 
#                         cv2.VideoWriter_fourcc(*'mp4v'), 
#                         20, frame_size)


# Write the video file to disk, 1 frame at a time
while(vid_capture.isOpened()):
    ret,frame = vid_capture.read()
    if ret == True:
        print('ret')
        # Write the frame to the output file
        output.write(frame)
    else:
        print('Stream disconnected')
        break
	
# Release the objects
vid_capture.release()
output.release()