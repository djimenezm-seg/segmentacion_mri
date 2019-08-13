import numpy as np

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

def DBSCAN_clustering(dataset):
	one_column = np.reshape(dataset, (-1,1)) # Lleva la imagen de entrada a una columna
	one_column_scaled = MinMaxScaler().fit_transform(one_column) # Normaliza el vector columna

	epsilon = 1/np.mean(one_column_scaled) # Se calcula epsilon para el algoritmo

	clusters = DBSCAN(eps=epsilon, min_samples=100).fit(one_column) # Aplica DBSCAN sobre la imagen

	return np.reshape(clusters.labels_, (dataset.shape[0], dataset.shape[1])) # Transforma y retorna el resultado de DBSCAN