def findClosetCentroids(X, initial_centroids):

    m = x.shape[0]
    K = initial_centroids.shape[0]
    dis = np.zeros((m, K))
    idx = np.zeros((m, 1))

    for i in range(m):
        for j in range(K):
            dis[i, j] = np.dot((X[i, :]-initial_centroids[j, :]).reshape(1, 01), (X[i,:] - initial_centroids[j, :]).reshape(-1,1))


    dummy, idx = np.where(dis == np.min(dis, axis=1).reshape(-1, 1))

    return idx[0:dis.shape[0]]


def computerCentroids(X, idx, K):

    n = X.shape[1]
    centroids = np.zeros((K, n))
    for i in range(K):
        centroids[i, :] = np.mean(X[np.ravel(idx == i), :], axis=0).reshape(1, -1)

    return centroids


def kMeansInitCentroids(X, K):
    m = X.shape[0]
    m_arr = np.arange(0, m)
    centroids = np.zeros((K, X.shape[1]))
    np.random.shuffle(m_arr)
    rand_indices = m_arr[:k]
    centroids = X[rand_indices, :]

    return centroids

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3).fit(X)
centroids = model.cluster_centers_

