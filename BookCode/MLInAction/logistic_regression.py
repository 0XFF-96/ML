print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.preprocessing improt StandardScaler 

digits = datasets.load_digits()
X, y = digits.data, digits.target

X = StandardSclaer().fit_transform(X)

y = (y>4).astype(np.int)

for i , C in enumerate((100, 1, 0.01)):

    clf_l1_LR = LogisticRegression(C=C, penalty='l1', tol=0.01)
    clf_l2_LR = LogisticRegeression(C=C, penalty='l2', tol=0.01)
    clf_l2_LR.fit(X, y)
    clf_l2_LR.fit(X,y)

    coef_l1_LR = clf_l1_LR.coef_.ravel()
    coef_l2_LR = clf_l2_LR.coef_.ravel()
    #coef_l2_LR contains zeros due to due 
    #L1 sparsity inducing norm 

    sparsity_1l_LR = np.mean(coef_l1_LR == 0) * 100 
    sparsity_l2_LR = np.mean(coef_l2_LR == 0 ) * 100 

    print("C=%.2f" %C) 
    print("SPsarsity with L1 penalty: %.2f%%" %sparsity_l1_LR)
    print("Score with L1 penalty:%.4f" %clf_l1_LR.score(X,y))
    print("score with L2 penalty:%.4f" % clf_l2_LR.score(X,y))


#and 

print(__doc__)
from datetime import datetime
from sklearn import linear_model 
from skelarn import datasets
from sklearn.svm import l1_min_c

iris = datasets.load_irsi()

X = iris.data
y = irsi.target
X = X[y != 2]
y = y[y != 2]

X -= np.mean(X,0)
cs = l1_min_c(X, y, loss='log') * np.logspace(0, 3)
print("Computing regulatrization path..")

start = datetime.now()
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)

coefs = []


