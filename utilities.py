import numpy as np
import nibabel as nib
#from nilearn import plotting
import matplotlib.pyplot as plt
#np.set_printoptions(threshold=np.nan)

def get_bounding_box(img_data_arr):
	ones = 0
	segm_index = []

	for imagen in range(img_data_arr.shape[2]):
		count_ones = np.count_nonzero(img_data_arr[:,:,imagen])	#(img_data_arr[imagen,:,:])

		if count_ones > 0:
			segm_index.append(imagen) 							#Lista de indices de las imagenes que contienen segmentacion (contienen unos)
			
		if count_ones > ones:
			ones = count_ones 									#Maxima cantidad de unos
			more_ones = imagen 									#Indice de la imagen que tiene la maxima cantidad de unos

	im_segm = img_data_arr[:,:,more_ones]#[more_ones,:,:]

	ones_coor = np.nonzero(im_segm) 							#Matriz de coordenadas de los puntos donde hay un uno
	first_row = ones_coor[0][0] 								#Primera fila donde aparece un uno
	first_column = np.amin(ones_coor[1]) 						#Primera columna donde aparece un uno
	last_row = ones_coor[0][-1]
	last_column = np.amax(ones_coor[1])

	begin_row = first_row-first_row/10 if first_row-first_row/10>=0 else 0

	end_row = last_row+last_row/10 if last_row+last_row/10<im_segm.shape[0] else im_segm.shape[0]-1

	begin_column = first_column-first_column/10 if first_column-first_column/10>=0 else 0

	end_column = last_column+last_column/10 if last_column+last_column/10<=im_segm.shape[1] else im_segm.shape[1]-1
	
	return begin_row, end_row, begin_column, end_column, segm_index

def cut_img(file_path, img_data_arr, begin_row, end_row, begin_column, end_column, segm_index, affine):

	ROI = np.zeros((end_row-begin_row, end_column-begin_column, len(segm_index)))

	for i, indexes in enumerate(segm_index):
		img = img_data_arr[:,:,indexes]
		img_cuts = img[begin_row:end_row,begin_column:end_column]
		ROI[:,:,i] = img_cuts

	file_name = file_path[:-4] + '-ROI.nii.gz'
	imgs = nib.Nifti1Image(ROI, affine)
	nib.save(imgs, file_name)
	return

def display_nifti(file_path):
	img_S = nib.load(file_path)
	img_S_data = img_S.get_data()
	img_S_data_arr = np.asarray(img_S_data)
	fig, axes = plt.subplots(nrows=1, ncols=img_S_data_arr.shape[2], figsize=(32, 32))
	axs = axes.flatten()
	for i in range(1):#(img_S_data_arr.shape[2]):		
		axs[i].set_axis_off()
		axs[i].set_title('imagen segmentada')
		axs[i].imshow(img_S_data_arr[:,:,i], cmap='bone')
	plt.show()
	return

def display_segmented(file_path):
	img_S = nib.load(file_path)
	img_S_data = img_S.get_data()
	img_S_data_arr = np.asarray(img_S_data)
	ones = 0
	segm_index = []

	for imagen in range(img_S_data_arr.shape[2]):
		count_ones = np.count_nonzero(img_S_data_arr[:,:,imagen])	#(img_data_arr[imagen,:,:])

		if count_ones > 0:
			segm_index.append(imagen) 							#Lista de indices de las imagenes que contienen segmentacion (contienen unos)
			
		if count_ones > ones:
			ones = count_ones 									#Maxima cantidad de unos
			more_ones = imagen 									#Indice de la imagen que tiene la maxima cantidad de unos
	print more_ones
	plt.axis('off')
	plt.suptitle(imagen)
	plt.imshow(img_S_data_arr[:,:,more_ones], cmap='bone')
	plt.show()

def display_cut(file_path, more_ones):
	img_S = nib.load(file_path)
	img_S_data = img_S.get_data()
	img_S_data_arr = np.asarray(img_S_data)
	ones = 0
	segm_index = []

	'''for imagen in range(img_S_data_arr.shape[2]):
		count_ones = np.count_nonzero(img_S_data_arr[:,:,imagen])	#(img_data_arr[imagen,:,:])

		if count_ones > 0:
			segm_index.append(imagen) 							#Lista de indices de las imagenes que contienen segmentacion (contienen unos)
			
		if count_ones > ones:
			ones = count_ones 									#Maxima cantidad de unos
			more_ones = imagen 									#Indice de la imagen que tiene la maxima cantidad de unos'''

	plt.axis('off')
	plt.suptitle(imagen)
	plt.imshow(img_S_data_arr[:,:,more_ones], cmap='bone')
	plt.show()

def cut_to_h5py(file_path, img_data_arr, begin_row, end_row, begin_column, end_column, segm_index, affine):

	ROI = np.zeros((end_row-begin_row, end_column-begin_column, len(segm_index)))

	for i, indexes in enumerate(segm_index):
		img = img_data_arr[:,:,indexes]
		img_cuts = img[begin_row:end_row,begin_column:end_column]
		ROI[:,:,i] = img_cuts

	'''file_name = file_path[:-4] + '-ROI.nii.gz'
	imgs = nib.Nifti1Image(ROI, affine)
	nib.save(imgs, file_name)'''
	return ROI