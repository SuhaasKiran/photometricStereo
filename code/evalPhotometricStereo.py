# This code is part of:
# 
#   COMPSCI 670: Computer Vision
#   University of Massachusetts, Amherst
#   Instructor: Grant Van Horn
# 
# Evaluation code for photometric stereo
# 
# Your goal is to implement the three functions prepareData(), 
# photometricStereo() and getSurface() to estimate the albedo and shape of
# the objects in the scene from multiple images. 
# 
# Start with setting subjectName='debug' which sets up a toy scene with
# known albedo and height which you can compare against. After you have a
# good implementation of this part, set the subjectName='yaleB01', etc. to
# run your code against real images of people. 
# 
# Credits: The homework is adapted from a similar one developed by
# Shvetlana Lazebnik (UNC/UIUC)


import os
import time
import numpy as np
import matplotlib.pyplot as plt 
import skimage.io as io

from utils import *
from getSurface import *
from photometricStereo import *
from loadFaceImages import *
from toyExample import *
from prepareData import *
from displayOutput import *
from displaySurfaceNormals import *
from alignShapeChannels import *

subjectName = 'yaleB07' #debug, yaleB01, yaleB02, yaleB05, yaleB07
numImages = 128
data_dir = os.path.join('..', 'data')
out_dir = os.path.join('..', 'output', 'photometricStereo')
image_dir = os.path.join(data_dir, 'photometricStereo', subjectName)
integrationMethod = 'random' #column-row, row-column, average, random

# Load images
print('Loading images.')
if subjectName == 'debug':
    imageSize = (64, 64) # Make this smaller to run your code faster for debugging
    (ambientImage, imArray, lightDirs, trueAlbedo, trueSurfaceNormals, trueHeightMap) = toyExample(imageSize, numImages)
else:
    (ambientImage, imArray, lightDirs) = loadFaceImages(image_dir, subjectName, numImages)

# Prepare data
print('Prepaing data.')
imArray = prepareData(imArray, ambientImage)

# Aligning all images with the first image
# max_shift = np.array([10, 10])
# a = imArray[:,:,0]
# pred_shifts = np.zeros(shape=(2,2,imArray.shape[2]))
# for i in range(imArray.shape[2]):
#     b = imArray[:,:,i]
#     imArray[:,:,i], pred_shifts[:,:,i] = alignShapeChannels(a, b.copy(), max_shift, method='cosine')

# imArray = imArray[10:b.shape[0]-10, 10:b.shape[1]-10, :]

print("imaArray shape - ", imArray.shape)
print("lightDirs shape - ", lightDirs.shape)

# Estimate albedo and normals
print('Estimating albedo and normals.')
(albedoImage, surfaceNormals) = photometricStereo(imArray, lightDirs)

# Estimate surface
print('Estimating surface height map.')
heightMap = getSurface(surfaceNormals, integrationMethod)

# Display outputs
displayOutput(albedoImage, heightMap)
displaySurfaceNormals(surfaceNormals)

# Display the true answer for debug
if subjectName == 'debug':
    displayOutput(trueAlbedo, trueHeightMap)
    displaySurfaceNormals(trueSurfaceNormals)

# Pause for input
x = input('[Done] Press any key to quit.')
