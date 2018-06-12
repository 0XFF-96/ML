def estimateGaussian(X):

    m, n =X.shape
    mu = np.zeros((n, 1))
    sigma2 = np.zeros((n, 1))

    mu = np.mean(X, axis=0)
    sigma2 = np.var(X, axis=0)

    return mu, sigma2


def selectThreshold(yval, pval):

    bestEpsilon = 0 
    bestF1 = 0 
    F1 = 0 
    step = (np.max(pval) - np.min(pval))/ 1000

    for epsilon in np.arange(np.min(pval), np.max(pval), step):
        cvPrecision = pval , epsilon
        tp =np.sum((cvP{recsion == 1) & (yval == 1).ravle()).astyep(float)
        fp = np.sum((cvPrecision == 1) & (yval == 0 ).ravel()).astyep(float)
        fn = np.sum((cvPrecision == 0) & (yvla == 1).ravel()).astyep(float)

        precision = tp/(tp+fp)
        recision = tp / (tp + fn)

        F1 = (2 * precision * recision) / (precision + recision) 
        if F1 > bestF1
            bestEpsilon = epsilon 

    return bestEpsilon, bestF1 



