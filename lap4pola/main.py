import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
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
        distances=[1],
        angles=[3 * np.pi / 4],
        symmetric=True,
        normed=False
    )
    cont = greycoprops(glcm, "contrast")[0, 0]
    diss = greycoprops(glcm, "dissimilarity")[0, 0]
    homo = greycoprops(glcm, "homogeneity")[0, 0]
    eng = greycoprops(glcm, "energy")[0, 0]
    corr = greycoprops(glcm, "correlation")[0, 0]
    ASM = greycoprops(glcm, "ASM")[0, 0]
    return [cont, diss, homo, eng, corr, ASM]

arr_dir = ["bata", "kayu"]
fnames = []
for a in range(len(arr_dir)):
    arr_tmp = [f for f in listdir(arr_dir[a]) if isfile(join(arr_dir[a], f ))]
    fnames.append(arr_tmp)

df = pd.DataFrame(columns = ["cont", "diss", "home", "eng", "corr", "ASM", "class"])
baris = 0
for i in range (len(arr_dir)):
    for j in range (len(fnames[i])):
        print(arr_dir[i] + "/" + fnames[i][j])
        avg = getDataTekstur(arr_dir[i] + "/" + fnames[i][j])
        print(avg)
        cont, diss, home, eng, corr, ASM = avg[0], avg[1], avg[2], avg[3], avg[4], avg[5]
        rows_list = [cont, diss, home, eng, corr, ASM, arr_dir[i]]
        df.loc[baris] = rows_list
        baris =baris + 1

cv2.waitKey(20)

print(df)
df.to_csv("data.csv", index = False, header = True)

arff.dump(
    "data.arff",
    df.values,
    relation = "Ekstraksi Warna Buah Mangga dan Salak",
    names = df.columns
)

g = sns.pairplot(df[["cont", "diss", "home", "eng", "corr", "ASM", "class"]], hue = "class", diag_kind = "hist")

plt.show()
