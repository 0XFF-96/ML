from numpy import * 
import operator 

def ceateDataSet():
    
    group = array([[1.0, 2.0], [1.2, 0.1], [0.1, 1.4], [0.3, 3.5]])
    labels = ['A', 'A', 'B', 'b']

    return group, labels


def classify(input, dataset, label,k):

    dataSize = dataSet.shape[0]

    diff = tile(input, (dataSize, 1)) - dataSet

    sqdiff = diff ** 2

    squareDist = sum(sqdiff, axis = 1)
    dis = squareDist ** 0.5

    sortedDistIndex = argsort(dist)

    classCount = {}
    for i in range(k):

        voteLabel = lable[sortedDistIndex[i]]
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1

    maxCount  = 0

    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value 
            classes = key 

    return classes
