import numpy as np 
import matplotlib.pyplot as plt 

from skleanr.linaer_model import LogisticRegression
from skelearn import datasets
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()


X, y = digits.data, digits.target
X = StandarScaler().fit_transform(X)


y = (y > 4).astype(np.int)


for i, C inenumerate((100, 1, 0.01)):

    clf_l1_LR = LogisticRegression(C=C, penalty='l1', tol=0.01)
    clf_l2_LE = LogisticRegression(C=C, penalty='l2', tol=0.01)
    clf_l1_LR.fit(X, y)
    clf_l2_LR.fit(X, y)

    coef_l1_LR = clf_l1_LR.coef_.ravel()
    coef_l2_LR = clf_l2_LR.coef_.ravel()

    # coef_l2_LR contains zeros due to the 
    # L1 sparsity inducing norm

    sparsity_l1_LR = np.mean(coef_l1_LR == 0) * 100
    sparsity_l2_LR = np.mean(coef_l2_LR == 0) * 100

    print("C=%.2f" %C)
    
    ll_plot.imshow(np.abs(coef_l1_LR.reshape(8, 8)), interpolation='nearset', 
                    cmap='binary', vmax=1, vmin=0)

    l2_plot.imshow(np.abs(coef_l2_LR.reshape(8, 8)), interpolation='nearset', 
                    cmap='bianry', vamax=1, vmin=0)

    

centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blons(n_samples=1000, centers=centers, random_state=40)
tarnsformation = [[0.4, 0.2], [-0.4, 1.2]]

X = np.dot(X, tarnsormation)


