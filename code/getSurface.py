import numpy as np
import random

def random_path(x, y, m, n, prev, depth, marked, surfaceNormals):
 
    # update the depth and marked for (x,y)
    if(x==0 and y==0):
        depth[x][y] = 0
        marked[x][y] = 1
    else:
        if(prev == 1):
            depth[x][y] = depth[x][y-1] + surfaceNormals[x,y,0]
        elif(prev == 2):
            depth[x][y] = depth[x-1][y] + surfaceNormals[x,y,1]
        else:
            pass
        marked[x][y] = 1

    # select next order of (x,y)
    next = random.randint(1,3)
    if(next == 1):
        # first go right
        if(y!=(n-1) and marked[x][y+1]==0):
            random_path(x, y+1, m, n, 1, depth, marked, surfaceNormals)
        # second go down
        if(x!=(m-1) and marked[x+1][y]==0):
            random_path(x+1, y, m, n, 2, depth, marked, surfaceNormals)
    
    else:
        # first go down
        if(x!=(m-1) and marked[x+1][y]==0):
            random_path(x+1, y, m, n, 2, depth, marked, surfaceNormals)
        # second go right
        if(y!=(n-1) and marked[x][y+1]==0):
            random_path(x, y+1, m, n, 1, depth, marked, surfaceNormals)
        
    return    


def getSurface(surfaceNormals, method):
    # print("inside normals shape - ", surfaceNormals.shape)
    surfaceNormals[:,:,0] = np.divide(surfaceNormals[:,:,0], surfaceNormals[:,:,2])
    surfaceNormals[:,:,1] = np.divide(surfaceNormals[:,:,1], surfaceNormals[:,:,2])
    depth = np.zeros(shape=(surfaceNormals.shape[0],
                            surfaceNormals.shape[1],), dtype=float)
    if method == 'row-column':
        for x in range(surfaceNormals.shape[0]):
            for y in range(surfaceNormals.shape[1]):
                if(x==0 and y==0):
                    depth[x][y] = 0
                elif(y==0):
                    depth[x][y] = depth[x-1][y] + surfaceNormals[x,y,1]
                else:
                    depth[x][y] = depth[x][y-1] + surfaceNormals[x,y,0]

        # raise NotImplementedError("You should implement this.")
    if method == 'column-row':
        for y in range(surfaceNormals.shape[1]):
            for x in range(surfaceNormals.shape[0]):
                if(x==0 and y==0):
                    depth[x][y] = 0
                elif(x==0):
                    depth[x][y] = depth[x][y-1] + surfaceNormals[x,y,0]
                else:
                    depth[x][y] = depth[x-1][y] + surfaceNormals[x,y,1]
        # raise NotImplementedError("You should implement this.")
    if method == 'average':
        # raise NotImplementedError("You should implement this.")
        row_col = getSurface(surfaceNormals, method="row-column")
        col_row = getSurface(surfaceNormals, method="column-row")
        depth = (row_col + col_row)/2
    if method == 'random':
        # raise NotImplementedError("You should implement this.")
        # n = numPaths()
        n = 5
        for count in range(n):
            currDepth = np.zeros(shape=(surfaceNormals.shape[0],
                            surfaceNormals.shape[1],), dtype=float)
            marked = np.zeros(shape=(surfaceNormals.shape[0],
                            surfaceNormals.shape[1],), dtype=int)
            random_path(0, 0, surfaceNormals.shape[0], surfaceNormals.shape[1],
                        0, currDepth, marked, surfaceNormals)
            
            depth += currDepth

        depth = depth/n

    return depth
