import scipy
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as distA
import numpy as np

##returns distance between two data points. alter this if data not binary
def dist(x, y):
    return sum (a != b for a,b in zip(x,y))


##takes a numpy matrix. returns distance matrix. 
def dist_matrix(data):

    dist_matrix = np.zeros((len(data), len(data)))
    for x in range(len(data)):
        for y in range(len(data)):
            if x == y:
                continue
            elif y > x:
                a = data[x]
                b = data[y]
                dist_matrix[x,y] = dist(a,b)
            else:
                dist_matrix[x,y] = dist_matrix[y,x]

    return dist_matrix

##returns a reordered data matrix based on results of hierarchal clustering. 
##clustering performed on rows, then columns. 

def hier_rearrange(data, column_label, row_label):

    distance = dist_matrix(data)
    sq = distA.squareform(distance)
    linkage = sch.linkage(sq)
    dendro = sch.dendrogram(linkage)
    leaves = dendro['leaves']

    ordered_rows = data[leaves,:]

    reordered_rlabel = []
    for index in leaves:
        reordered_rlabel.append(row_label[index])

    distance2 = dist_matrix(ordered_rows.T)
    sq2 = distA.squareform(distance2)
    linkage2 = sch.linkage(sq2)
    dendro2 = sch.dendrogram(linkage2)
    leaves2 = dendro2['leaves']


    fully_reordered = (ordered_rows.T[leaves2,:]).T
    reordered_clabel = []



    for index in leaves2:
        reordered_clabel.append(column_label[index])

    return fully_reordered, reordered_clabel, reordered_rlabel


