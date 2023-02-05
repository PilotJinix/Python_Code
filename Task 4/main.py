
from check import *
import numpy as np
import pandas as pd
import pprint
import warnings
import statistics
warnings.filterwarnings('ignore')


cars = pd.read_csv("cars_clean.csv")
cars["Merk"] = [data.split()[0] for data in cars.Car]
cars["Merk"].nunique()
cek_jawaban(cars, "1a")
cars_specs = cars[["Car", "Merk", "MPG", "Horsepower", "Acceleration", "Origin"]]
cek_jawaban(cars_specs, "1b")

changeType = {
    "Car": 'str',
    "Merk": 'category',
    "MPG": float,
    "Horsepower": 'int64',
    "Acceleration": float,
    "Origin": 'category'
}
cars_specs = cars_specs.astype(changeType)

cars_specs.iloc[:,0:6].info()
cek_jawaban(cars_specs.iloc[:,0:6], "1c")

cars_specs["Tenaga"] = np.where(
    cars_specs.Horsepower == 100, 'Normal',
    np.where(
        cars_specs.Horsepower < 100, 'Selow','Super'
    )

)

cars_specs["Tenaga"].value_counts()
cek_jawaban(cars_specs, "2a")

kondisi =[cars_specs.MPG > 25, cars_specs.MPG < 25, cars_specs.MPG == 25]
result = ["Hemat", "Boros", "Normal"]
cars_specs["Efisiensi"] = np.select(kondisi, result, 0)

# print((cars_specs["Efisiensi"] == "Hemat").sum())
cars_specs["Efisiensi"].value_counts()
cek_jawaban(cars_specs, "2b")

kondisi_rekomendasi = [(cars_specs.Tenaga == 'Super') & (cars_specs.Efisiensi == 'Hemat'), (cars_specs.Tenaga == 'Selow') & (cars_specs.Efisiensi == 'Boros')]
result_rekomendasi = ["Bagus", "Jelek"]
cars_specs["Rekomendasi"] = np.select(kondisi_rekomendasi, result_rekomendasi, "Lumayan")

cars_specs["Rekomendasi"].value_counts()
cek_jawaban(cars_specs, "2c")

mobil, tenaga, efisiensi, rekomendasi = data_list(cars_specs)

mobil1 = ['Buick Century', 'Oldsmobile Cutlass LS', 'Ford Grenada gl']
tenaga1 = ['Super', 'Super', 'Selow']
efisiensi1 = ['Boros', 'Hemat', 'Boros']
rekomendasi1 = ['Lumayan', 'Bagus', 'Jelek']

identitas = {}

for i in range(len(mobil1)):
    identitas[mobil1[i]]= {"Tenaga": tenaga1[i], "Efisiensi": efisiensi1[i], "Rekomendasi":rekomendasi1[i]}

pprint.pprint(identitas)
cek_jawaban(identitas, "3")

def rata_rata(data):
    additional = 0
    for i in range(len(data)):
        additional += data[i]
    return additional / len(data)

rata_rata(cars["Weight"])
cek_jawaban(cars, "4a", rata_rata(cars["Weight"]))


# def varians(data):
#     rata = rata_rata(data)
#     hitung = 0
#     for i in data:
#         hitung += (i - rata) ** 2
#     hitung /=len(data)
#     return hitung ** (1/2)

def varians(data):
    rata = rata_rata(data)
    dev= [(x - rata) ** 2 for x in data]
    hasil = 0.000
    for i in dev:
        hasil +=i
    return hasil / len(data)

varians(cars["Weight"])
cek_jawaban(cars, "4b", varians(cars["Weight"]))

def standar_deviasi(data):
    return varians(data) ** 0.5

standar_deviasi(cars["Weight"])
cek_jawaban(cars, "4c", standar_deviasi(cars["Weight"]))

vokal = ["A", "I", "U", "E", "O"]
fix_letter = []
vokal = ["A", "I", "U", "E", "O"]


vokal = ["A", "I", "U", "E", "O"]
def gabungan(data):
    cek = False
    for i in range(len(data)):
        if data[i] in vokal:
            print('\n', data[i], end='')
            cek = True
        else:
            if cek == True:
                print(' - ', end='')
                print(data[i], end='')

gabungan(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
gabungan(['B','E','A','C','D','J','I','R','S','T','L','K','N','U','M','H','G','P','F','Q','V','O','W','X','Y','Z'])
gabungan(['B','C','M','E','D','J','G','R','S','T','L','K','N','Z','A','H','I','P','F','Q','V','O','W','X','Y','U'])


nilai = int(input('Anggka'))
usia = int(input('usia'))


if nilai >= 75:
    if usia < 15:
        print("Selamat dik, Kamu lulus!")
    else:
        print("Selamat Kak, Kamu lulus!")
# elif nilai >= 80:
#     print(80)
# elif nilai >= 60:
#     print(60)
# elif nilai >= 40:
#     print(40)
else:
    # print('else')
    if usia < 15:
        print("Mohon Maaf dik, Coba Lagi ya!")
    else:
        print("Mohon Maaf Kak, Coba Lagi ya!")


for i in range(1,4):
    print(i)