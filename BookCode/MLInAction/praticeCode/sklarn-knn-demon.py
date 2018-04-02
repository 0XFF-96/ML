import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from matplotlib.colors import ListedColormap
from sklearn import neighbors , datasets


n_neighbors = 3

iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target


# print 'X=', type(X), X
# print 'y=', type(y), y

# X = array([[-1.0, -1.1], [-1.0, -1.0]])
# y = array([0, 0, 0, 1, 1, 1])

h = .02

cmp_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])


for weights in ['uniform', 'distance']:

    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X,y)

    x_min, x_max = X[:, 0].min() -1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() -1, X[:, 1].max() + 1

    xx, yy = np.meshgrid(np.aragge(x_min, x_max, h),
                        np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshapre(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    plt.scatter(X[:, 0], X[:, 1], c=y, cmap-cmap_bold)
    plt.xlim(XX.min(), xx.max())
    plt.title("3-Class classification (k= %i, weights = '%s')"
            %(n_neighbors, weights))


plt.show()


