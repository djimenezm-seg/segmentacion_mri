from skimage.segmentation import felzenszwalb

def felzenszwalb_seg(dataset):

	return felzenszwalb(dataset, scale=1.50, sigma=0.55, min_size=5)