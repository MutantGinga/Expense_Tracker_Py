from sklearn.cluster import KMeans

def cluster_transactions(X, n_clusters=10):

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    labels = kmeans.fit_predict(X)
    return kmeans, labels
