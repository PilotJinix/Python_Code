import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import arff
import seaborn as sns
from os import listdir
from os.path import isfile, join

def getDataTekstur(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    modus = np.max(gray)
    median = np.median(gray)
    rentang = np.max(gray)-np.min(gray)
    euclidean = np.linalg.norm(gray)
    

    return [modus, median, rentang, euclidean ]

# list directory
arr_dir = ['bata','kayu']
fnames = []
for a in range(len(arr_dir)):
    # get all files name
    arr_tmp = [f for f in listdir(arr_dir[a]) if isfile(join(arr_dir[a],f))]
    fnames.append(arr_tmp)
df = pd.DataFrame(columns=['modus', 'median', 'rentang', 'euclidean', 'class'])
baris = 0

for i in range(len(arr_dir)):
    for j in range(len(fnames[i])):
        print(arr_dir[i]+'/'+fnames[i][j])
        avg = getDataTekstur(arr_dir[i]+'/'+fnames[i][j])
        print(avg)
        modus, median, rentang, euclidean = avg[0], avg[1], avg[2], avg[3]
        rows_list = [modus, median, rentang, euclidean, arr_dir[i]]
        df.loc[baris] = rows_list
        baris = baris + 1

cv2.waitKey(20)

print(df)
# simpan format csv
df.to_csv ('data.csv', index = False, header=True)

# simpan format weka arff
arff.dump('data.arff'
    , df.values
    , relation='Ekstraksi Warna Buah Mangga dan Salak'
    , names=df.columns)

g = sns.pairplot(df[['modus', 'median', 'rentang', 'euclidean', 'class']], hue="class",
diag_kind="hist")

plt.show()
