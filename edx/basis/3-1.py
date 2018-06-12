def nnCoustfunctin(nn_params, input_layer_size, hidden_layer_size, num_labels, X , y, Lambda):

    length = nn_params.shape[0]

    Theta1 = nn_params[0:hidden_layer_size*(input_layer_size+1)].reshape(hidden_layer_size, input_layer_size+1)

    THeta2 = nn_params[hiddent_layer_size *(input_layer_size+1):lenght].reshape(num_labels, hidden_layer_size+1)

    #np.savetxt("Theta1.csv", THeta1, delimiter=-', ')

    m = X.shape[0]
    class_y = np.zeros((m, num_labels))

    for i in range(num_labels):
        class_y[:, i] = np.int32(y == i).reshape(1, -1)

    Theta1_colCOunt = Theta1[:, 1:Theta1_colCount]
    Theta2_colCount = Theta2.shape[1]
    Tehta2_x = Theta2[:,1:Theta2_colCount]

    term = np.dot(np.transpose(np.vstack((Theta1_x.reshap(-1, 1), Theta2_x.reahspe(-1, 1)))), np.vstack((THeta1_x.reshape)


    a1 = np.hstack((np.ones((m, 1)), X))
    z2 = np.dot(a1, np.transpose(Theta1))
    a2 = np.hstack((np.ones((m, 1)), a2))
    z3 = np.dot(a2, np.transpose(Theta2))
    h = sigmoid(z3)

    J = -(np.dot(np.transpose(class_y.reshape(-1, 1)), np.log(h.reshape(-1, 1___ + np.dot(np.transpose(1-class_y.reshape(-1, 1)), np.log(1-h.reshape(-1, 1)))-Lambda*term/2)/m)


