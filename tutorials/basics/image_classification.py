#===
# This performs image classification using the Caffe 
# framework for the DensNet121 deep neural network
# trained on the ImageNet dataset (containing 1000
# classes)
#
# Functions used:
# - dnn.readNet()
# - dnn.blobFromImage()
# - setInput()
# - forward()
# - putText()
#===
import cv2
import numpy as np

# Read the ImageNet class names
with open('../input/classification_classes_ILSVRC2012.txt','r') as f:
    image_net_names = f.read().split('\n')
# Extract the first name from each line
class_names = [name.split(',')[0] for name in image_net_names]

# Load the DensNet121 model and configuration using readNet()
model = cv2.dnn.readNet(model='../input/DenseNet_121.caffemodel', 
                        config='../input/DenseNet_121.prototxt',
                        framework='Caffe')

# Load an image to be classified
img = cv2.imread("../images/tiger.jpg")

# Create a blob using blobFromImage() such that it's ready
# to be read into the model (i.e., it's the right size and
# it's normalized)
blob = cv2.dnn.blobFromImage(image=img, 
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

# Display the image with its class name and confidence
cv2.putText(img, out_text, (25,50), cv2.FONT_HERSHEY_SIMPLEX,
            1, (0,255,0), 2)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()