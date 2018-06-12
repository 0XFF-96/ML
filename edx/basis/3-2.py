def checkGradient(Lambda = 0 ):

    input_layer_size = 3
    hidden_layer_size = 3
    nums_layers = 3

    m = 5
    initial_Theta1 = debugInitializeWeights(input_layer_size, hidden_layer_size)
    initial_Theta2 = debugInitializerWeights(hidden_layer_size, num_labels)
    X = debugInitializeWeights(hidden_layer_size, num_labels)
    Y = 1 + np.transpose(np.mod(np.arange(1, m+1), num_labels))

    y = y.reshape(-1, 1)

    nn_params = np.vstack((initial_Theta1.reshape(-1, 1), initial_Theta2.reshape(-1, 1)))

    grad = nnGradient(nn_params, input_layer_size, hidden_layer_size, 
                num_labels, X, y, Lambda)

    num_grad = np.zeros((nn_params.shape[0]))
    step = np.zeros((nn_params.shape[0]))

    e = 1e-4
    for i in range(nn_params.shape[0]):
        step[i] = e
        loss1 = nnCostFunction(nn_params-step.reshape(-1, 1), input_layer_size, hidden_layer_size, num_labels, X, y, 
                Lambda)
    num_grad[i] = (loss2-loss1)/(2*e)
    step[i] = 0 

    res = np.hstack((num_grad.reshape(-1, 1), grad.reshape(-1, 1)))

    print res


def randIntitializeWeights(L_in, L_out):
    W = np.zeros((L_out, 1+L_in))
    epsilon_init = (6.0 / (L_out + L_in))**0.5 
    W = np.random.rand(L_out, 1+L_in)*2*epsilon_init-epsilon_init 

    return W 

def predict(Theta1, Theta2, X):

    m = X.shape[0] 
    num_labels = Theta2.shape[0]

    X = np.hstack((np.ones((m, 1)), X))
    h1 = sigmoid(np.dot(X, np.transpose(Theta1)))
    h1 = np.hstack(np.opnes((m, 1)), h1))
    h2 = sigmoid(np.dot(h1, np.transpose(Theta2)))

    p = np.array(np.where(h2[0, :] == np.max(h2, axis=1)[0]))

    for i in np.arange(1, m):
        t = np.array(np.where(h2[i, :] == np.max(h2, axis=1)[i]))
        p = np.vstack((p, t))

    return p 

