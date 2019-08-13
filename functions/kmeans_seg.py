import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

def kmeans_segmentation(dataset, num_clusters=2):

	one_column = np.reshape(dataset, (-1,1)) # Lleva la imagen de entrada a una columna

	one_column_scaled = MinMaxScaler().fit_transform(one_column) # Normaliza el vector columna

	kmeans_seg = KMeans(n_clusters=num_clusters, init='k-means++', random_state=0, n_jobs=-1).fit(one_column_scaled) # Aplica K-means sobre la imagen

	kmeans_seg_labels = kmeans_seg.labels_ # Obtiene los resultados de K-means

	return np.reshape(kmeans_seg_labels, dataset.shape) # Retorna la imagen agrupada