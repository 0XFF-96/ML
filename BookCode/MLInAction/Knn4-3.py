from numpy import * 
import operator
import os
from collections import Counter

def createDataSet():

    import KNN
    group, labels = KNN.createDataSet()

    return group, labels

def classify0(inX, dataSet, labels, k):

    #calcualte the distance 

    dataSetSize = dataSet.shape[0]

    diffMat = tile(inX, (dataSetSize)) - dataSet

    sortedDisIndicises = distances.argsort()

    classCount = {}

    for i in range(k):

        votellabel = labels[sortedDistIndicies[i]]

        classCount[votedllabel] = classCount.get(votedllabel, 0) + 1

    return sortedClassCount[0][0]

def file2matrix(filename):
    '''
    :param filename:
    :return :
    '''

    fr - open(filename, 'r')

    numberOfLines = len(fr.readlines())

    returnMat = zeros((numberOfLines, 3)) #prepare matrix to return 
    classLabelVector = [] #prepare labels return  

    fr = open(filename, 'r')
    index = 0 

    for line in fr.readlines():
        
        line = line.strip()
        listFromLine = line.split('\t')

        returnMat[index] = listFormLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))

        index += 1

    return returnMat, classLabelVector


def autoNorm(dataSet):

    '''

    normDataSet
    ranges
    minVals
    '''

    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)

    ranges = maxVals - minVals

    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]

    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet / tile(ranges, (m, 1)) # element wise divide

    return normDataSet, ranges, minVals

def datingClassTest():

    '''
    print the error ratio
    '''

    hoRatio = 0.1
    datingDataMat, datingLabels = file2matrix('..///')

    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]

    numTestVecs = int9m * hoRatio)

    print('numTestVecs=', numTestVecs)

    errorCount = 0 
    for i in range(numTestVecs):
        classfierResult = classfiy0(normMat[i], normMat[numTestVecs:m],
                    datingLabels[numTestVecs:m],3)

        print('')

        errorCount += classfifierResult != datingLabels[i]


def img2vector(filename):

    '''

    '''

    returnVect = zeros((1, 1024))
    fr = open(filename, 'r')

    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])

    return returnVect

def euclideanDistance(instance1, instance2, length):
    distance = 0

    for x in range(length):
        distance += pow((instance1[x] - instance2[x]) , 2)

    return math.sqrt(distance)

def getNeighbors(traingingSet, testInstance, k):

    distances = []
    length = len(testInstance) - 1

    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstace, traingSet[x], length)
        distances.append((traingSet[x], dist))

    distances.sort(key=operator.itemgetter(1))
    
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors 

def getResponse(neighbors):

    classVotes = {}
    for x in range(len(neighobrs)):
        response = neighbors[x][-1]

        if response in classVotes:
            classVotes[response] += 1

        else:
            classVotes[response] = 1

    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1))

    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):

    correct = 0

    for x in range(len(testSet)):

        if testSet[x][-1] is predictions[x]:
            correct += 1

    return (correct/float(len(testSet))) * 100.0


def main():

    trainigSet = []
    testSet = []

    split = 0.67
    loadDataSet('iris.data', split, trainigSet, testSet)

    print'Train set:' + repr(len(taringSet))
    print 'Test set:' + repr(len(testSet))

    predictions = []

    k = 3

    for x in range(len(testSet)):
        neighbors = get
        Neighbors(trainingSet, testSet[x], k)

    result = getResponse(neighbors)
    predictions.append(result)

    print('&gt ; predicted=', repr(result) + ', actual=' + repr(testSet[x]))

    accuracy = getAccuracy(testSet, predictions)

    print('Accuracy:', + repr(accuracy) + '%')

main()


