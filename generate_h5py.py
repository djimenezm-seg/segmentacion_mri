import os
import h5py
import numpy as np
import nibabel as nib
from utilities import *

f = h5py.File("dataset_cuello.hdf5", "w")

#first_group = f.create_group("dataset_cuello")

for dirname, dirnames, filenames in os.walk('./dataset_cuello/'):#('./Registradas_y_segmentadas/'): #('..\..'):

	for i, name in enumerate(filenames): 

		if i == 0:
			groups = f.create_group(dirname[1:])#first_group.create_group(dirname[1:])

		
		if 'S' in name:
			print name
			print 'dirname = {}'.format(dirname[1:]) #(dirname.split('/')[1])
			file_path = os.path.join(dirname, name)
			img_S = nib.load(file_path)
			img_S_data = img_S.get_data()
			img_S_data_arr = np.asarray(img_S_data)

			begin_row, end_row, begin_column, end_column, segm_index = get_bounding_box(img_S_data_arr)

	for name in filenames:

		file_path = os.path.join(dirname, name)
		img_S = nib.load(file_path)
		img_S_data = img_S.get_data()
		img_S_data_arr = np.asarray(img_S_data)
		ROI = cut_to_h5py(file_path[:-3], img_S_data_arr, begin_row, end_row, begin_column, end_column, segm_index, img_S.affine)

		dset = groups.create_dataset(name, ROI.shape, ROI.dtype, data=ROI)
