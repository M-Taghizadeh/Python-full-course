import os
import sys
import cv2
import numpy as np

# Create data matrix from a list of images
def createDataMatrix(images):
	print("Creating data matrix",end=" ... ", flush=True)
	numImages = len(images)
	sz = images[0].shape ### (218, 178, 3)
	data = np.zeros((numImages, sz[0] * sz[1] * sz[2]), dtype=np.float32)
	for i in range(0, numImages):
		image = images[i].flatten()
		data[i,:] = image
	
	print("DONE")
	return data

# Read images from the directory
def readImages(path):
	print("Reading images from " + path, end=" ... ", flush=True)
	images = []
	# List all files in the directory and read points from text files one by one
	for filePath in sorted(os.listdir(path)):
		fileExt = os.path.splitext(filePath)[1]
		if fileExt in [".jpg"]:
			# Add to array of images
			imagePath = os.path.join(path, filePath)
			im = cv2.imread(imagePath)
			# # Convert image to floating point
			im = np.float32(im)/255.0 
			# Add image to list
			images.append(im)

	numImages = len(images)
	# Exit if no image found
	if numImages == 0 :
		print("No images found")
		sys.exit(0)

	print(str(numImages) + " files read.")
	return images

# Directory of my dataset:
dirName = "C:/Users/Zanis/Desktop/AI Docs/AI02/PCA/images/"
# Read images
images = readImages(dirName)
# Size of images
sz = images[0].shape # return a tuple for me 
# Create data matrix for PCA.
data = createDataMatrix(images)
# Compute the eigenvectors from the stack of images created
print("Calculating PCA ", end=" ... ", flush=True)
mean, eigenVectors = cv2.PCACompute(data, mean=None, maxComponents=int(len(data)*0.50)) # 1)maxcomponetn is number of eigenface (between 1 to number of dataset) 2) mean and eigenVectors is vector...
cv2.imshow('Mean', mean.reshape(sz))
cv2.waitKey(0)
cv2.destroyAllWindows()
### write .yml data file
filename = "C:/Users/Zanis/Desktop/AI Docs/AI02/PCA/newDB.yml"
print("Writing size, mean and eigenVectors to " + filename, end=" ... ", flush=True)
file = cv2.FileStorage(filename, cv2.FILE_STORAGE_WRITE)
file.write("mean", mean) 
file.write("eigenVectors", eigenVectors)
file.write("size", sz)
file.release()
print("DONE")