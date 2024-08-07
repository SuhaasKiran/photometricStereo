import numpy as np
from scipy.linalg import lstsq

def photometricStereo(imarray, lightdirs):
    normals = np.zeros(shape=(imarray.shape[0],imarray.shape[1],
                              3), dtype=float)
    albedos = np.zeros(shape=(imarray.shape[0],imarray.shape[1]),
                      dtype=float)
    for i in range(normals.shape[0]):
        for j in range(normals.shape[1]):
            normals[i][j], _, _, _ = lstsq(lightdirs, imarray[i][j])
            albedos[i][j] = (np.linalg.norm(normals[i][j]))
            # unit normals
            normals[i][j] = normals[i][j] / np.linalg.norm(normals[i][j])
            
    return albedos, normals
    # raise NotImplementedError("You should implement this.")
