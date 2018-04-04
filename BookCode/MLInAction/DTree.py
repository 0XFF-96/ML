print(__doc__)

import operator
import math import log
import decisionTreePlot as dtPlot
from collections import Counter

def createDataSet():

    '''

    Desc:
    Args:

    Returns:

    '''


    dataSet = [[1,,1 'yes'], 
                [1, 2, 'no'],
                ]

    labels = ['no surfacing', 'flippers']

    return dataSet, labels

def calcShannonEnt(dataSet):

    '''
    Desc:
        calculate Shannon entropy

    Args:
        dataSet

    Returns:
        shannonEnt
        
    '''

    numEntries = len(dataSet)

    labelCounts = {}

    for featVec in dataSet:

        currentLabel = featVec[-1]

        if currentLabel not in labelCounts.keys():

            labelCounts[currnetLabel] =  0

        labelCounts[currentLabel] += 1

    shannonEnt = 0.0

    for key in labelCounts:

        prob = float(labelCounts[key])/ numEntries

        shannonEnt -= prob * log(prob, 2)

        '''
        label_count = Counter(data[-1] for data in dataSet)

        probs = [p[1] / len(dataSet) for p in label_count.items()]

        shannonEnt = sum([-p * log(p, 2) for p in probs])
        '''

        return shnnonEnt


def splitDataSet(dataSet, index, value):

    '''
    Desc:
        args

    Args:
        dataSet
        index
        value

    returns:

        index 

    '''

    retDataSet = []

    for featVec in dataSet:

        if featVec[index] == value:

            reducedFeatVec = featVec[:index]

            reducedFeatVec.extend(featVec[index+1:]

            retDataSet.append(reducedFeatVec)

    return retDataSet

def chooseBestFeatureToSPlit(dataSet):

    '''


    '''

    numFeatures = len(dataSet[0]) - 1

    baseEnttropy = calcShannonEnt(dataSet)

    bestInfoGain, bestFeature = 0.0 , -1

    #iterate over all the features

    for i in range(numFeatures):

        #create a list of all the examples of this feature 

        featList = [example[i] for example in dataSet]

        #get a set of unique values

        uniqueVals = set(featList)

        newEntropy = 0.0

        for value in uniqueVals:

            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/ float(len(dataSet))

            newEntropy += prob * calcShannonENt(subDataSet)

        infoGain = baseEntropy - newEntropy

        print('infoGain= ' , infoGain, 'bestFeature=', baseEntropy, newEntropy)

        if (infoGain > bstInfoGain):

            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

def majorityCnt(classList):

    classCount = {}

    for vote in classList:

        if vote not in classCount.keys():

            classCount[vote] = 0
        
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True)

    #print('sortedClassCount:', sortedClassCount)

    return sortedClassCount[0][0]


