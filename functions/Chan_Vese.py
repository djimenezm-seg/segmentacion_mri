import numpy as np
from skimage import img_as_float
from skimage.segmentation import chan_vese


def Chan_Vese(dataset):

	image = img_as_float(dataset) # Carga la imagen

	init_mat = np.zeros(dataset.shape) # Crea la matriz de inicio del algoritmo

	init_mat[dataset.shape[0] - 1:-(dataset.shape[0] - 1), dataset.shape[1] - 1:-(dataset.shape[1] - 1)] = 1 # Define la matriz de inicio del algoritmo

	cv = chan_vese(image, mu=0.8, lambda1=3, lambda2=1, tol=1e-3, max_iter=200,
	               dt=0.25, init_level_set=init_mat, extended_output=True) # Aplica Chan-Vese sobre la imagen

	return cv[0] # Retorna la imagen segmentada 