#===
# This script performs real-time image classification
# on webcam feed
#===
import cv2
import numpy as np

# Setup the neural network model
with open('../tutorials/input/classification_classes_ILSVRC2012.txt','r') as f:
    image_net_names = f.read().split('\n')
class_names = [name.split(',')[0] for name in image_net_names]
model = cv2.dnn.readNet(model='../tutorials/input/DenseNet_121.caffemodel', 
                        config='../tutorials/input/DenseNet_121.prototxt',
                        framework='Caffe')
# Setup webcam settings
webcam = cv2.VideoCapture(0)
fps    = 60
period = int(1000 / fps)

ret = True
while ret:
    # Capture a frame
    ret, frame = webcam.read()

    # Create a blob using blobFromImage() such that it's ready
    # to be read into the model (i.e., it's the right size and
    # it's normalized)
    blob = cv2.dnn.blobFromImage(image=frame, 
                                scalefactor=0.01,
                                size=(224,224),
                                mean=(104,117,123))

    # Set the blob as the input for the network
    model.setInput(blob)

    # Forward propagation
    outputs = model.forward()

    # Reshape the output vector
    final_outputs = outputs[0]
    final_outputs = final_outputs.reshape(1000,1)

    # Get the index for the largest output
    label_id = np.argmax(final_outputs)

    # Convert output vector to probabilities and find the highest
    # probability
    probs = np.exp(final_outputs) / np.sum(np.exp(final_outputs))
    final_prob = np.max(probs) * 100

    # Find the class corresponding to this label
    out_name = class_names[label_id]
    out_text = f"{out_name}, {final_prob:.3f}"

    # Display the frame
    # Display the image with its class name and confidence
    cv2.putText(frame, out_text, 
                (25,50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0,0,0), 2)
    cv2.imshow("Webcam capture", frame)
    cv2.waitKey(period)

# Release the object
webcam.release()