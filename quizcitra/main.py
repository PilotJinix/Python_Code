import cv2
import numpy as np


img = cv2.imread("agung1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gambar = cv2.imread("agung1.png",0)
konversi = cv2.equalizeHist(gambar)
result = np.hstack((gambar,konversi))

cv2.imshow("Gambar Awal",img)
cv2.imshow("Gambar setelah grayscale",gray)
cv2.imshow("Hasil ",result)
cv2.waitKey(0)
cv2.destroyAllWindows()


