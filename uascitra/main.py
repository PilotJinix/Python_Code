import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import pandas as pd

# ### ===============Erosi Dilasi========================Meli
# img = cv2.imread('40.png',0)
# def getRata2BGR(img_path):
#         h,w,ch = img.shape
#         imgCopy = img.copy()
#
#         # nilai threshold
#         bbr, bbg, bbb = 128,128,128 # batas bawah
#         bar, bag, bab = 255,225,255 # batas atas
#
#         batas_bawah = np.array((bbr, bbg, bbb), np.uint8)
#         batas_atas = np.array((bar, bag, bab), np.uint8)
#         img_threshold = cv2.inRange(imgCopy, batas_bawah, batas_atas)
#
#         bgrGry = cv2.cvtColor(img_threshold, cv2.COLOR_GRAY2BGR)
#         imgHasil = cv2.bitwise_and(imgCopy, bgrGry, img_threshold)
#
#         avg_color_per_row = np.average(imgHasil, axis=0)
#         avg_color = np.average(avg_color_per_row, axis=0)
#
#         jml_nonzero = cv2.countNonZero(img_threshold)
#
#         avg_color = avg_color * (h*w)/jml_nonzero
#
#         return avg_color
#
# kernel = np.ones((5,5),np.uint8)
# erosi = cv2.erode(getRata2BGR(img),kernel,iterations = 3)
# dilasi = cv2.dilate(getRata2BGR(img),kernel,iterations = 3)
#
# cv2.imshow('src', img)
# cv2.imshow('erosi', erosi)
# cv2.imshow('dilasi', dilasi)
# cv2.waitKey(0)

# ===============Erosi Dilasi========================
# img = cv2.imread('40.png',0)
# ret,thresh1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
#
# img = cv2.resize(thresh1, (300,400))
#
# kernel = np.ones((5,5),np.uint8)
# erosi = cv2.erode(img,kernel,iterations = 3)
# dilasi = cv2.dilate(img,kernel,iterations = 3)
#
# cv2.imshow('src', img)
# cv2.imshow('erosi', erosi)
# cv2.imshow('dilasi', dilasi)
# cv2.waitKey(0)

# ## ===============Brigthness dan contras========================
# img = cv2.imread("40.png")
#
# contrast = 1.0 # Simple contrast control
# brightness = 100 # Simple brightness control
# imgbaru = np.zeros(img.shape, img.dtype) #membuat citra kosong dengan ukuran dan type yang sama
#
# for y in range(img.shape[0]):
#         for x in range(img.shape[1]):
#                 for c in range(img.shape[2]):
#                         imgbaru[y,x,c] = np.clip(contrast*img[y,x,c] + brightness, 0, 255)
#
# cv2.imshow('Citra Lena Awal', img)
# cv2.imshow('Citra Lena Setelah Pencerahan', imgbaru)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # ===============Threshold========================
# img = cv2.imread("40.png")
# ret, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
# cv2.imshow('Threshold', thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ## ===============Segmentasi garis========================
# import cv2, os, sys
#
# img = cv2.imread("garis.png")
#
# # kernel point detection
# # ~ kernel = np.array((
# 	# ~ [-1, -1, -1],
# 	# ~ [-1, 8, -1],
# 	# ~ [-1, -1, -1]), dtype="int")
# # kernel horisontal
# kernelHor = np.array((
# 	[-1, -1, -1],
# 	[2, 2, 2],
# 	[-1, -1, -1]), dtype="int")
# kernelVertikal = np.array((
# 	[-1, 2, -1],
# 	[-1, 2, -1],
# 	[-1, 2, -1]), dtype="int")
# kernel45 = np.array((
# 	[-1, -1, 2],
# 	[-1, 2, -1],
# 	[2, -1, -1]), dtype="int")
# kernelMin45 = np.array((
# 	[2, -1, -1],
# 	[-1, 2, -1],
# 	[-1, -1, 2]), dtype="int")
#
#
# horImg = cv2.filter2D(img,-1,kernelHor)
# vertImg = cv2.filter2D(img,-1,kernelVertikal)
# img45 = cv2.filter2D(img,-1,kernel45)
# imgMin45 = cv2.filter2D(img,-1,kernelMin45)
# orImg = cv2.bitwise_or(horImg, vertImg)
# orImg2 = cv2.bitwise_or(orImg, img45)
# orImgAll = cv2.bitwise_or(orImg2, imgMin45)
#
# cv2.imshow("img src", img)
# cv2.imshow("horImg", horImg)
# cv2.imshow("vertImg", vertImg)
# cv2.imshow("img45", img45)
# cv2.imshow("imgMin45", imgMin45)
# cv2.imshow("orImg", orImg)
# cv2.imshow("orImgAll", orImgAll)
# cv2.waitKey(0)

# # ## ===============Segmentasi lubang========================
# img = cv2.imread('seranganUlat.png')
# Z = img.reshape((-1,3))
#
# # convert to np.float32
# Z = np.float32(Z)
#
# # define criteria, number of clusters(K) and apply kmeans()
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# K = 2
# ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
#
# print('ret: ', ret)
# print('label: ', label)
# print('center: ', center)
# # Now convert back into uint8, and make original image
# center = np.uint8(center)
# res = center[label.flatten()]
# res2 = res.reshape((img.shape))
#
# cv2.imshow('img',img)
# cv2.imshow('res2',res2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


def getRata2BGR(img_path):
    img = cv2.imread(img_path)
    imgCopy = img.copy()

    # nilai threshold
    bbr, bbg, bbb = 150,150,0 # batas bawah
    bar, bag, bab = 255,255,255 # batas atas

    batas_bawah = np.array((bbr, bbg, bbb), np.uint8)
    batas_atas = np.array((bar, bag, bab), np.uint8)
    img_threshold = cv2.inRange(imgCopy, batas_bawah, batas_atas, cv2.THRESH_BINARY)

    gambarthresholding = cv2.resize(img_threshold, (512,512))

    # cek image
    cv2.imshow('Gambar Thresholding', gambarthresholding)
    cv2.imshow('Gambar', img)


# list directory
arr_dir = ['nangka']
fnames = []
for a in range(len(arr_dir)):
    # get all files name
    arr_tmp = [f for f in listdir(arr_dir[a]) if isfile(join(arr_dir[a],f))]
    fnames.append(arr_tmp)

for i in range(len(arr_dir)):
    for j in range(len(fnames[i])):
        print(arr_dir[i]+'/'+fnames[i][j])
        avg = getRata2BGR(arr_dir[i]+'/'+fnames[i][j])
        cv2.waitKey(1000)



# ===============Erosi Dilasi========================
# img = cv2.imread('40.png',0)
# ret,thresh1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
#
# img = cv2.resize(thresh1, (300,400))
#
# kernel = np.ones((5,5),np.uint8)
# erosi = cv2.erode(img,kernel,iterations = 3)
# dilasi = cv2.dilate(img,kernel,iterations = 3)
#
# cv2.imshow('src', img)
# cv2.imshow('erosi', erosi)
# cv2.imshow('dilasi', dilasi)
# cv2.waitKey(0)