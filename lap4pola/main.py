import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas
import arff
import seaborn as sns
from os import listdir
from os.path import isfile, join
from skimage import io
from skimage.feature import greycomatrix, greycoprops

def getDataTekstur(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    glcm = greycomatrix(
        gray,
        distances=[1, 2],
        angles=[0, np.pi/4, np.pi/2, 3*np.pi/4],
        symmetric=True,
        normed=False
    )
    cont = greycoprops(glcm, "Contrast")[0, 0]
    diss = greycoprops(glcm, "dissimilarity")[0, 0]
    homo = greycoprops(glcm, "homogeneity")[0, 0]
    eng = greycoprops(glcm, "energy")[0, 0]
    corr = greycoprops(glcm, "correlation")[0, 0]
    ASM = greycoprops(glcm, "ASM")[0, 0]
    return [cont, diss, homo, eng, corr, ASM]

arr_dir = ["bata", "kayu"]