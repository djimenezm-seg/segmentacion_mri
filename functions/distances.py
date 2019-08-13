import numpy as np
import scipy.spatial as sp

def Kernel(data, sigma):
    """
    On Spectral Clustering: Analisys and an algorithm
    Andrew Y. Ng - Michael I. Jordan - Yair Weiss
    Entradas
    data = Matriz de caracteristicas
    sigma = Ancho de banda del kernel
    """
    m_dis = sp.distance_matrix(data, data)
    A = np.exp(-m_dis/(2.0*sigma**2.0))    
    return A