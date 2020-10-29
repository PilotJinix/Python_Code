import cv2 #import library cv2
import numpy as np
img = cv2.imread("tomat.png")
contrast = 1.0 # Simple contrast control
brightness = 100 # Simple brightness control
imgbaru = np.zeros(img.shape, img.dtype) #membuat citra kosong dengan ukuran dan type yang sama

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            imgbaru[y,x,c] = np.clip(contrast*img[y,x,c] + brightness, 0, 255)
            
cv2.imshow('Citra Lena Awal', img)
cv2.imshow('Citra Lena Setelah Pencerahan', imgbaru)
cv2.waitKey(0)
cv2.destroyAllWindows()
