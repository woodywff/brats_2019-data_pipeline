import numpy as np
import pdb

def minmax_normalize(img_npy):
    '''
    img_npy: ndarray
    '''
    min_value = np.min(img_npy)
    max_value = np.max(img_npy)
    return (img_npy - min_value)/(max_value - min_value)

def print_red(something):
    print("\033[1;31m{}\033[0m".format(something))
    
