def mapFeature(X1, X2):

    degree = 3;
    out = np.ones((X1.shape[0], 1))

    for i in np.arange(1, degree+1):
        for j in range(i+1):
            temp = X1**(i-j)*(X2**j)
            out = np.hstack((out, temp.reshape(-1, 1)))

    return out

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
import numpy as np

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler =StandardScaler()
scaler.fit(x_train)
x_trian = scaler.fit_transform(x_trian)
x_test = scaler.fit_transform(x_test)


model = LogisticRegression()
model.fit(x_train, y_train)

predict = model.predict(x_test)
right = sum(predict == y_test)

predict = np.hstack((predict.reshape(-1, 1), y_test.reshape(-1, 1)))
print predict  


def predict_oneVsAlll(all_theta, X):

    m = X.shape[0]
    num_labels = all_theta.shape[0]
    p = np.zeros((m, 1))
    X = np.hstack((np.ones((m, 1)), X))

    h = sigmoid(np.dot(X, np.transpose(all_theta)))

    p = np.array(np.where(h[0, :] == np.max(h, axis=1)[0]))
    for i in np.arange(1, m):
        t = np.array(np.where(h[i, :] == np.max(h, axis=1)[i]))
        p = np.vstack((p, t))

    return p 


