import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.preprocessing import MinMaxScaler

def mean_shift(dataset):
	one_column = np.reshape(dataset, (-1,1))
	one_column_scaled = MinMaxScaler().fit_transform(one_column)

	x = np.array(range(dataset.shape[0]))
	y = np.array(range(dataset.shape[1]))
	X, Y = np.meshgrid(x, y)
	X = np.reshape(X, (-1,1))
	Y = np.reshape(Y, (-1,1))
	three_column = np.concatenate((one_column, Y, X), axis=1)
	three_column_scaled = MinMaxScaler().fit_transform(three_column)

	bandwidth = estimate_bandwidth(one_column_scaled, quantile=0.2, n_samples=500)
	clustering = MeanShift(bandwidth=bandwidth).fit(one_column_scaled)
	clustering_labels = clustering.labels_#*100
	return np.reshape(clustering_labels, (dataset.shape[0], dataset.shape[1]))