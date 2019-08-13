import numpy as np
import h5py

from functions.kmeans_seg import kmeans_segmentation
from functions.Chan_Vese import Chan_Vese
from functions.DBSCAN_clust import DBSCAN_clustering

from sklearn.metrics import adjusted_rand_score, accuracy_score

from skimage.filters import threshold_sauvola

from utilities import *

npr_cv = []
accuracy_cv = []

npr_kmeans = []
accuracy_kmeans = []

npr_dbscan = []
accuracy_dbscan = []

def segment_sequence(name, obj):

	temp_slice_S = []
	temp_slice_T = []

	if 'T1' in name: # 

		paciente = f[name.rsplit('/', 1)[0]]

		for secuencia in paciente:
			imagen = f[name.rsplit('/', 1)[0]+'/'+secuencia]

			if 'S' in secuencia:
				temp_slice_S = imagen

			if 'T1' in secuencia:
				temp_slice_T = imagen

		for i in range(temp_slice_S.shape[2]):

			sliced_T = temp_slice_T[:,:,i]
			sliced_S = temp_slice_S[:,:,i]

			smoothened_sliced = threshold_sauvola(sliced_T, window_size=9, k=0.08, r=None)

			cv = Chan_Vese(smoothened_sliced)
			kmeans = kmeans_segmentation(smoothened_sliced)
			dbscan = DBSCAN_clustering(sliced_T)

			npr_cv.append(adjusted_rand_score(cv.astype(sliced_S.dtype).flatten(), sliced_S.flatten()))
			accuracy_cv.append(accuracy_score(sliced_S.flatten(), cv.astype(sliced_S.dtype).flatten(), normalize=True))

			npr_kmeans.append(adjusted_rand_score(kmeans.astype(sliced_S.dtype).flatten(), sliced_S.flatten()))
			accuracy_kmeans.append(accuracy_score(sliced_S.flatten(), kmeans.astype(sliced_S.dtype).flatten(), normalize=True))

			npr_dbscan.append(adjusted_rand_score(dbscan.astype(sliced_S.dtype).flatten(), sliced_S.flatten()))
			accuracy_dbscan.append(accuracy_score(sliced_S.flatten(), dbscan.astype(sliced_S.dtype).flatten(), normalize=True))

		temp_slice_S = []
		temp_slice_T = []

f = h5py.File("mytestfile.hdf5", "r")
f.visititems(segment_sequence)

print 'Resultado de NPR para Chan-Vese: {}'.format(np.mean(npr_cv))
print 'Resultado de Accuracy para Chan-Vese: {}'.format(np.mean(accuracy_cv))
print 'Resultado de NPR para kmeans: {}'.format(np.mean(npr_kmeans))
print 'Resultado de Accuracy para kmeans: {}'.format(np.mean(accuracy_kmeans))
print 'Resultado de NPR para dbscan: {}'.format(np.mean(npr_dbscan))
print 'Resultado de Accuracy para dbscan: {}'.format(np.mean(accuracy_dbscan))
