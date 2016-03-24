'''
Created on Jan 26, 2015

@author: edwingsantos
'''

if __name__ == '__main__':
    pass

"""
from sklearn import datasets
digits = datasets.load_digits()
print "Digit: ", digits.target[0]
print digits.images[0]
print 'Feature vector \n', digits.images[0].reshape(-1, 64)
"""

import numpy as np
from skimage.feature import corner_harris, corner_peaks
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.exposure import equalize_hist


def showCorners(corners, image):
    fig = plt.figure()
    plt.gray()
    plt.imshow(image)
    y_corner , x_corner = zip(*corners)
    plt.plot(x_corner,y_corner, 'or')
    plt.xlim(0,image.shape[1])
    plt.ylim(image.shape[0], 0)
    fig.set_size_inches (np.array(fig.get_size_inches()) * 1.5)
    print "X: ", x_corner,"\nY: " , y_corner
    plt.show()
    
    
    
mandrill = io.imread('mandrill.png')
mandrill = equalize_hist(rgb2gray(mandrill))
corners = corner_peaks(corner_harris(mandrill), min_distance=2)
showCorners(corners, mandrill)
     
    
    
