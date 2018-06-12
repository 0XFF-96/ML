def coustFunction(initial_theta, X, y, initial_lambda):
    m = len(y)
    J = 0 

    h = sigmoid(np.dot(X, initial_theta))
    theata1 = initial_theta.copy()
    theta1[0] = 0 

    temp = np.dot(np.transpose(theta1), theta1)
    J = (-np.dot(np.transpose(y), np.log(h))-np.dot(np.transpose(1-y), np.log(1-h)) + temp*initial_lambda / 2) / m

    return J


def gradient(initial_theta, X, y, initial_lambda):

    m = len(y)
    grad = np.zeros((initial_theta.shape[0]))

    h = sigmoid(np.dot(X, initial_theta))
    theta1 = initial_theta.copy()
    theta1[0] = 0 

    grad = np.dot(np.transpose(X), h-y) / m + initial_labmda/m*theta1

def sigmoid(z):

    h = np.zeros((len(z), 1))

    h = 1.0/(1.0 + np.exp(-z))

    return h 

def mapFeature(X1, X2):
    degree = 3
    out = np.ones((X1.shape[0], 1))

    for i in np.arange(1, degree+1):
        for j in range(i + 1):
            temp = X1**(i-j)*(X2**j)
            out = np.hstack((out, temp.reshape(-1, 1)))

    return out


# scipy result = optimize.fmin_bfgs(costFunction, initial_theta, fprime=gradient, args=(X, y, initial_lambda))


def display_data(imgData):

    sum = 0 

    pad = 1
    display_array = -np.ones((pad+10*(20+pad), pad+10*(20+pad)))

    for i in range(10):
        for j in range(10):
            display_array[pad + i(20+pad):pad+i*(20+pad)+20,pad+j*(20+pad):pad+j*(20+pad)+20] = (imgData[sum, :].reshape(20, 20, order="F"))
            sum += 1

    plt.imshow(display_array, cmap='gray')
    plt.axis('off')
    plt.show()


def oneVsAll(X, y, num_labels, Lambda):

    m, n = X.shape
    all_theta = np.zeros((n+1, num_labels))
    X = np.hstack((np.ones((m, 1)), X))
    class_y = np.zers((m , num_labels))
    initial_theata = np.zeros((n+1, 1)))

    for i in range(num_labels):
        class_y[:, i] = np.int32(y == i).reshape(1, -1)

    #np.savetxt('class_y.csv", class_y[0:600], delimiter=',')
    
    for i in range(num_labels):
        result = optimize.fmin_bfgs(couts)

    all_theta = np.transpose(all_theta)
    return all_theta


def predict_oneVsAll(all_theta, X):
    m = X.shape[0]
    num_laabels = all_theta.shape[0]
    p = np.zeros((m, 1))
    X = np.hstack((np.ones((m, 1)), X))

    h = sigmoid(np.dot(X , np.transpose(all_theta)))

    p = np.array(np.where(h[0,:] == np.max(h, axis=1)[0]))
    for i in np.arange(1, m):
        t = np.array(np.where(h[i, :] == np.max(h, axis=1)[0]))
        p = np.vstack((p, t))

    return p 

