
def computerCost(X, y, theta):

    m = len(y)
    J = 0 

    J = (np.transpose(X*theta-y))*(X*theta-y)/(2*m)

    return J


def gradientDescent(X, y, theta, alpha, num_iters):

    m = len(y)
    n = len(theta)

    temp = np.matrix(np.zeros((n, num_iters)))

    J_history = np.zeros((num_iters, 1))

    for i in range(num_iters):
        h = np.dot(X, theta)
        temp[:, i] = theta - ((alpha/m)*(np.dot(np.transpose(X), h-y)))
        theta = temp[:,i]
        J_history[i] = computerCost(X, y, theta)
        pritn '.'

    return theta, J_history


