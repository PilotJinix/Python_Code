import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import arff
import seaborn as sns
from os import listdir
from os.path import isfile, join

def getRata2BGR(img_path):
    img = cv2.imread(img_path)
    h,w,ch = img.shape[:]
    imgCopy = img.copy()

    # nilai threshold
    bbr, bbg, bbb = 0,0,0 # batas bawah
    bar, bag, bab = 200,200,200 # batas atas

    batas_bawah = np.array((bbr, bbg, bbb), np.uint8)
    batas_atas = np.array((bar, bag, bab), np.uint8)
    img_threshold = cv2.inRange(imgCopy, batas_bawah, batas_atas)

    bgrGry = cv2.cvtColor(img_threshold, cv2.COLOR_GRAY2BGR)
    imgHasil = cv2.bitwise_and(imgCopy, bgrGry, img_threshold)

    avg_color_per_row = np.average(imgHasil, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)

    jml_nonzero = cv2.countNonZero(img_threshold)

    avg_color = avg_color * (h*w)/jml_nonzero

    # cek image
    cv2.imshow('bgrGry', bgrGry)
    cv2.imshow('imgHasil', imgHasil)
    cv2.imshow('img', img)
    return avg_color

# list directory
arr_dir = ['Angka_Delapan','Angka_Sembilan']
fnames = []
for a in range(len(arr_dir)):

    # get all files name
    arr_tmp = [f for f in listdir(arr_dir[a]) if isfile(join(arr_dir[a],f))]
    fnames.append(arr_tmp)

df = pd.DataFrame(columns=['b', 'g', 'r', 'class'])
baris = 0
for i in range(len(arr_dir)):
    for j in range(len(fnames[i])):
        print(arr_dir[i]+'/'+fnames[i][j])
        avg = getRata2BGR(arr_dir[i]+'/'+fnames[i][j])
        print(avg)
        ab,ag,ar = avg
        rows_list = [ab,ag,ar,arr_dir[i]]
        df.loc[baris] = rows_list
        baris = baris + 1

cv2.waitKey(20)

print(df)
# simpan format csv
df.to_csv ('data.csv', index = False, header=True)

# simpan format weka arff
arff.dump('data.arff'
    , df.values
    , relation='Ekstraksi Warna Angka Delapan dan Angka Sembilan'
    , names=df.columns)
plt.figure()
sns.scatterplot(data = df
                ,x = 'b'
                ,y = 'g'
                ,hue = 'class'
                )
plt.figure()
sns.scatterplot(data = df
                ,x = 'b'
                ,y = 'r'
                ,hue = 'class'
                )
plt.figure()
sns.scatterplot(data = df
                ,x = 'g'
                ,y = 'r'
                ,hue = 'class'
                )
plt.show()
