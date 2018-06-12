
def featureNormalize(X):

    n = X.shape[1]
    mu = np.zeros((1,n))
    sigma = np.zeros((1, n))

    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)

    for i in range(n):
        X[:, i] = (X[:, i] - mu[i]) /sigma[i]

    
    return X, mu, sigma


Sigma = np.dot(np.transpose(X_norm), X_norm) / m 

U, S, V = svd()

def projectData(X_norm, U, K):

    Z = np.zeros(X_norm.shape[0], K))

    U_reduce = U[:, 0:K]
    Z = np.dot(X_norm, U_reduce)

    return Z

def reoverData(Z, U, K):

    X_rec = np.zeros((Z.shape[0], U.shape[0]))
    U_reduce = U[:, 0:K]
    X_rec = np.dot(Z, np.transpose(U_redece))

    return X_rec 

project error: 1 / m 
total variation : error ratio 
-=-=-=-=-=-=-=-===--=-=-=


import numpy as np
from matplotlib import pyplot as plt
from scipy import io as spio
from skleanr.decomposition import pca
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
scaler.fit(X)
x_train = scaler.stransform(X)

n_components

K=1 
model = pca.PCA(n_components=K).fit(x_train)
Z = model.transform(x_trian)

model.components_
Urduce = model.components_
x_rec = np.dot(Z, Ureduce)

import numpy as np
from matplotlib import pyplot as plt
from scipy import io as spio
from sklearn.decomposition import pca


def PCA_2d():
    data_2d = spio.loadmat('data.mat')
    X = data_2d['X']
    m = X.shape[0]
    plt = plot_data_2d(X, 'bo')
    plt.show()

    X_copy = X.copy()
    X_norm, mu, sigma = featureNormalize(X_copy)

    Sigma = np.dot(np.transpone(X_norm), X_norm) / m 
    U, S, V = np.linalg.svd(Sigma)

    plt = plot_data_2d(X, 'bo')
    drawline(plt, mu, mu+S[0]*(U[:, 0]), 'r-')

    plt.axis('squre')
    plt.show()

    K = 1
    Z = projectData(X_norm, U, K)
    X_rec = recoverData(Z, U, K)

    plt = plt_data_2d(X_norm, 'bo')
    plot_data_2d(X_rec, 'ro')

    for i in range(X_norm.shape[0]):
        drawline(plt, X_norm[i, :], X_rec[i, :], '--k')

    plt.axis('square')
    plt.show()

def PCA_faceImage():
    print ('..')
    data_iamge = spio.loadmat('data_faces.mat')
    X = data_iamge['X']
    display_iamgeData(X[0:100,:])
    m = X.shape[0]

    print('...')
    X_norm, mu, sigma = featureNormalize(X)

    Sigma = np.dot(np.transpose(U[:, 0:36]))

    print ('..')
    K = 100 
    Z = projectDadta(X_norm, U, K)

    print('...')

    

