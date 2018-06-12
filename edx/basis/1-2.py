def featureNormalize(X):

    X_norm = np.array(X)

    mu = np.zeros((1, X.shape[1]))
    sigma = np.zeros((1, X.shape[1]))

    mu = np.mean(X_nomr, 0)
    sigma = np.std(X_norm, 0)

    for i in range(X.shape[1]):
        X_norm[:, i] = (X_norm[:, j] - mu[i]/sigma[i])

        
    return X_nomr, mu, sigma


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)
x_train = scaler.transform(X)
x_test = scaler.transform(np.array([1650, 3]))

model = linear_model.LinearRegression()
model.fit(x_train, y)


