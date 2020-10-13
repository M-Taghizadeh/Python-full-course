import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def displayResult(left, right)	:
	output = np.hstack((left,right))	
	output = cv2.resize(output, (0,0), fx=4, fy=4)
	cv2.imshow("Result", output)

# Recontruct face using mean face and EigenFaces
def reconstructFace(*args):
	# Start with the mean / average face
	output = averageFace
	for i in range(0,args[0]):
		weight = np.dot(imVector, eigenVectors[i])
		output = output + eigenFaces[i] * weight
	displayResult(im, output)

# Read model file
modelFile = "C:/Users/Zanis/Desktop/AI Docs/AI02/PCA/newDB.yml"
file = cv2.FileStorage(modelFile, cv2.FILE_STORAGE_READ)

# Extract mean vector
mean = file.getNode("mean").mat()

# Extract Eigen Vectors
eigenVectors = file.getNode("eigenVectors").mat()

# Extract size of the images used in training
sz = file.getNode("size").mat()
sz = (int(sz[0,0]), int(sz[1,0]), int(sz[2,0]))
print("size of eigenfaces : ", sz)
numEigenFaces = eigenVectors.shape[0] # shape[0] get size of eigenvectors..

# Extract mean vector and reshape it to obtain average face
averageFace = mean.reshape(sz)

# Reshape Eigenvectors to obtain EigenFaces
eigenFaces = [] 
for eigenVector in eigenVectors:
    eigenFace = eigenVector.reshape(sz)
    eigenFaces.append(eigenFace)

# Read new test image. This image was not used in traning. 
imageFilename = "C:/Users/Zanis/Desktop/AI Docs/AI02/PCA/images/000052.jpg"
im = cv2.imread(imageFilename)
im = np.float32(im)/255.0 # Convert to floating point image

# Reshape image to one long vector and subtract the mean vector
imVector = im.flatten() - mean; 


# Display EigenFaces
#####################################################################
i = 0
list_frame = []
for eigenFace in eigenFaces:
	weight = np.dot(imVector, eigenVectors[i])
	list_frame.append(eigenFace * weight)
	i = i+1
	print(weight)
final_frame = cv2.hconcat(list_frame)
fig=plt.figure(figsize=(8, 8))
number_of_selected = len(eigenVectors)*0.2
columns = 8
rows = int(number_of_selected / columns)+1
for i in range(1, columns*rows + 1):
    fig.add_subplot(rows, columns, i)
    plt.imshow(list_frame[i - 1])
plt.show()
#####################################################################

# Show mean face first
output = averageFace

# Create window for displaying result
cv2.namedWindow("Result", cv2.CV_32SC4)

# Changing the slider value changes the number of EigenVectors
# used in reconstructFace.
cv2.createTrackbar( "No. of EigenFaces", "Result", 0, numEigenFaces, reconstructFace )

# Display original image and the reconstructed image size by side
displayResult(im, output)
cv2.waitKey(0)
cv2.destroyAllWindows()
