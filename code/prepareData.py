import numpy as np

def prepareData(imArray, ambientImage):
    imArray = imArray - ambientImage[:, :, np.newaxis]
    np.where(imArray < 0, 0, imArray) 
    imArray = imArray/imArray.max()
    return imArray
    # raise NotImplementedError("You should implement this.")
