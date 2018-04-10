import matplotlib.pyplot as plt
import numpy as np 
from sklearn import svm 


def loadDataSet(fileName):

    '''
    '''

    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(fload(lineArr[2]))

    return dataMat, LabelMat 

X, y = loadDataSet('..')
X = np.mat(X)

clf = svm.SVC(kernel='linear')
clf.fit(X, y)

w = clf.coef[0]

a = -w[0] / w[1]

yy = a * xx - (clf.intercerpt_[0] / w[1])
print("yy=", yy)

#plot the parallels to the separating hyperplane that pass through the support vectors 
print ("Support vectors = ", clf.support_vectors)
b = clfsupport_vectors[0]

yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

#plot the line , the points, and the nearest vectors to the plane 
plt.plot(xx, yy, 'k-')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k__')


plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:,1], s=80, facecolors='none')
plt.scatter(X[:, 0].flat, X[:, 1].flat, c=Y, cmap=plt.cm.Paired)


plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:,1], s=80, facecolors='none')
plt.scatter(X[:, 0].flat, X[:, 1].flat, c=Y, cmap=plt.cm.Paired)



