from sklearn import cluster

k = 2
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(data)
