# import cv2 #import library cv2
#
# import numpy as np  #import library cv2
#
# filegambar = "tomat.png"  #Mengalamatkan variabel filegambar kepada file tomat.png
#
# gambar = cv2.imread(filegambar)    #Memuat gambar kedalam variabel gambar dengan memasukkan alamat file gambar
#
# gambar1 = gambar * 2 #Hasil gambar yang berupa nilai matriks akan dikalikan 2
#
# hsv = cv2.cvtColor(gambar, cv2.COLOR_BGR2HSV) #memberikan warna pada gambar dengan menggunakan hsv agar mempertajam dari tiap warnanya atau mendeteksi ketajaman warna
#
# #hsv adalah penentuan nilai batas atas dan batas bawah untuk mendeteksi objek berdasarkan warna
#
# #BGR sistem pewarnaan 3 dimensi (Blue, Green, Red)
#
# #HSV (Hue, Saturation, Value (tingkat kecerahan))
#
# h,s,v = cv2.split(hsv) #Split berati memasukkan data kedalam tiap variabel h,s,v
#
# h = 2 * h #pada matrik v pada gambar tomat di 2 kali tingkatkan
#
# hsv1 = cv2.merge((h,s,v)) #digunakan untuk menggabungkan hasil seluruh gambar
# hsv1 = cv2.cvtColor(hsv1, cv2.COLOR_HSV2BGR) #merubah warna dari hsv ke semula
#
# cv2.imshow("Gambar ", gambar) #Menampilkan Hasil gambar
# cv2.imshow("Gambar 1", gambar1) #Menampilkan Hasil gambar
# cv2.imshow("HSV ", hsv) #Menampilkan Hasil gambar
# cv2.imshow("HSV1 ", hsv1) #Menampilkan Hasil gambar
#
# cv2.waitKey(0) #delay destroy windows


# import cv2 #import library cv2
# import numpy as np
# img = cv2.imread("tomat.png")
# contrast = 1.0
# brightness = 500
# imgbaru = np.zeros(img.shape, img.dtype)
#
# for y in range(img.shape[0]):
#     for x in range(img.shape[1]):
#         for c in range(img.shape[2]):
#             imgbaru[y] = np.clip(contrast*img[y] + brightness,0,255)
#
# cv2.imshow('Gambar Tomat Awal', img)
# cv2.imshow('Gambar Tomat Setelah Pencerahan', imgbaru)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# img = cv2.imread("tomat.png")
#
# alpha =2
# beta = 50
#
# result =cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)
#
# cv2.imshow('Gambar Tomat Awal', img)
# cv2.imshow('Gambar Tomat Setelah Pencerahan', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import numpy as np
# import cv2
#
# img = cv2.imread ('tomat.png')
# k = 3
# kernelBlur = np.ones ((k,k), np.float32) / (k*k)
# imgBlur1 = cv2.filter2D (img, -1, kernelBlur)
# cv2.imshow ('imgBlur1', imgBlur1)
#
# k = 5
# kernelBlur = np.ones ((k,k), np.float32) / (k*k)
# imgBlur2 = cv2.filter2D (img, -1, kernelBlur)
# cv2.imshow ('imgBlur2', imgBlur2)
#
# k = 7
# kernelBlur = np.ones ((k,k), np.float32) / (k*k)
# imgBlur3 = cv2.filter2D (img, -1, kernelBlur)
# cv2.imshow ('imgBlur3', imgBlur3)
#
# k = 9
# kernelBlur = np.ones ((k,k), np.float32) / (k*k)
# imgBlur4 = cv2.filter2D (img, -1, kernelBlur)
# cv2.imshow ('imgBlur4', imgBlur3)
# cv2.waitKey(0)

import numpy as np
from matplotlib import pyplot as plt
import cv2

# Load image
img = cv2.imread('tomat.png')

# Create kernel
kernel3x3 = np.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
    ])
kernel5x5 = np.array([
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, 25, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1]
    ])
kernel7x7 = np.array([
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 49, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1]
    ])
kernel9x9 = np.array([
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 81, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]
])

# Sharpen image
imgSharp3x3 = cv2.filter2D(img, -1, kernel3x3)
imgSharp5x5 = cv2.filter2D(img, -1, kernel5x5)
imgSharp7x7 = cv2.filter2D(img, -1, kernel7x7)
imgSharp9x9 = cv2.filter2D(img, -1, kernel9x9)

# Show image
cv2.imshow('img', img)
cv2.imshow('imgSharp3x3', imgSharp3x3)
cv2.imshow('imgSharp5x5', imgSharp5x5)
cv2.imshow('imgSharp7x7', imgSharp7x7)
cv2.imshow('imgSharp9x9', imgSharp9x9)

cv2.waitKey(0)




