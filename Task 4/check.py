import matplotlib.pyplot as plt
import pandas as pd
import pprint
        
def cek_jawaban(data, nomor, hasil=None):

    try:

        # Nomor 1 - A
        if nomor == "1a":
            for merek in data["Merk"].unique():
                if merek in ['Chevrolet', 'Buick', 'Plymouth', 'AMC', 'Ford', 'Pontiac',
                            'Citroen', 'Dodge', 'Toyota', 'Datsun', 'Volkswagen', 'Peugeot',
                            'Audi', 'Saab', 'BMW', 'Chevy', 'Hi', 'Mercury', 'Opel', 'Fiat',
                            'Oldsmobile', 'Chrysler', 'Mazda', 'Volvo', 'Renault', 'Honda',
                            'Subaru', 'Chevrolete', 'Capri', 'Mercedes-Benz', 'Cadillac',
                            'Mercedes', 'Triumph', 'Nissan']:
                    continue
                else:
                    print("❌ SALAH, periksa isi dari kolom Merk")
                    break
            else:
                if data["Merk"].nunique() == 34:
                    print("✅ BENAR")
                else:
                    print(f"❌ SALAH, terdapat {data['Merk'].nunique()} merek")

        # Nomor 1 - B
        elif nomor == "1b":
            for kolom in data.columns:
                if kolom in ["Car", "Merk", "MPG", "Horsepower", "Acceleration", "Origin"]:
                    continue
                else:
                    print("❌ SALAH, pastikan kolom sudah sesuai")
                    break
            else:
                if (data.shape[0] == 406) & (data.shape[1] == 6):
                    print("✅ BENAR")
                elif (data.shape[0] == 406):
                    print(f"❌ SALAH, terdapat {data.shape[1]} kolom")
                elif (data.shape[1] == 6):
                    print(f"❌ SALAH, terdapat {data.shape[0]} baris")
                else:
                    print(f"❌ SALAH, terdapat {data.shape[1]} kolom dan {data.shape[0]} baris")

        # Nomor 1 - C
        elif nomor == "1c":
            if (data["Car"].dtype == "object") & \
                (data["Merk"].dtype == "category") & \
                    (data["MPG"].dtype == "float64") & \
                        (data["Horsepower"].dtype == "int64") & \
                            (data["Acceleration"].dtype == "float64") & \
                                (data["Origin"].dtype == "category"):
                print("✅ BENAR")
            else:
                print("❌ SALAH, silakan periksa tipe datanya\n")
                for kolom in data.columns:
                    print(f"{kolom.ljust(12)} : {data[kolom].dtype}")

        # Nomor 2 - A
        elif nomor == "2a":
            if ((data["Tenaga"] == "Selow").sum() == 232) & \
                ((data["Tenaga"] == "Super").sum() == 157) & \
                    ((data["Tenaga"] == "Normal").sum() == 17):
                print("✅ BENAR")
            else:
                print(
                    f"❌ SALAH, terdapat {(data['Tenaga'] == 'Selow').sum()} Selow, {(data['Tenaga'] == 'Super').sum()} Super, dan {(data['Tenaga'] == 'Normal').sum()} Normal")
    
        # Nomor 2 - B
        elif nomor == "2b":
            if ((data["Efisiensi"] == "Boros").sum() == 237) & \
                ((data["Efisiensi"] == "Hemat").sum() == 158) & \
                    ((data["Efisiensi"] == "Normal").sum() == 11):
                print("✅ BENAR")
            else:
                print(
                    f"❌ SALAH, terdapat {(data['Efisiensi'] == 'Boros').sum()} Boros, {(data['Efisiensi'] == 'Hemat').sum()} Hemat, dan {(data['Efisiensi'] == 'Normal').sum()} Normal")

        # Nomor 2 - C
        elif nomor == "2c":
            if ((data["Rekomendasi"] == "Lumayan").sum() == 326) & \
                ((data["Rekomendasi"] == "Jelek").sum() == 73) & \
                    ((data["Rekomendasi"] == "Bagus").sum() == 7):
                print("✅ BENAR")
            else:
                print(
                    f"❌ SALAH, terdapat {(data['Rekomendasi'] == 'Lumayan').sum()} Lumayan, {(data['Rekomendasi'] == 'Jelek').sum()} Jelek, dan {(data['Rekomendasi'] == 'Bagus').sum()} Bagus")

        # Nomor 3
        elif nomor == "3":
            if (data['Buick Century']['Rekomendasi'] == 'Lumayan') & \
                (data['Oldsmobile Cutlass LS']['Rekomendasi'] == 'Bagus') & \
                    (data['Ford Grenada gl']['Rekomendasi'] == 'Jelek'):
                print("✅ BENAR")
            else:
                print("❌ SALAH, silakan periksa dictionary yang dihasilkan\n")
                pprint.pprint(data)

        # Nomor 4 - A
        elif nomor == "4a":
            if round(hasil, 4) == round(data["Weight"].mean(), 4):
                print("✅ BENAR")
            else:
                print(f"❌ SALAH, rata-rata yang didapatkan adalah {round(hasil, 4)} ... dari yang seharusnya {round(data['Weight'].mean(), 4)}")

        # Nomor 4 - B
        elif nomor == "4b":
            if round(hasil, 4) == round(data["Weight"].var(), 4):
                print("✅ BENAR")
            else:
                print(f"❌ SALAH, varians yang didapatkan adalah {round(hasil, 4)} ... dari yang seharusnya {round(data['Weight'].var(), 4)}")

        # Nomor 4 - C
        elif nomor == "4c":
            if round(hasil, 4) == round(data["Weight"].std(), 4):
                print("✅ BENAR")
            else:
                print(f"❌ SALAH, standar deviasi yang didapatkan adalah {round(hasil, 4)} ... dari yang seharusnya {round(data['Weight'].std(), 4)}")

        # Nomor 5
        elif nomor == "5":
            print("Anggap saja ✅ BENAR, namun pastikan hasilnya sudah sesuai yang diharapkan")

        # Lainnya
        else:
            print(f"❓ Nomor {nomor} tidak ditemukan")

    except:
        print("⚠️ ERROR")


def boxplot(data, kolom):

    df = pd.DataFrame({col:vals[kolom] for col, vals in data.groupby("Merk")})
    meds = df.max().sort_values(ascending=False)
    df[meds.index].boxplot(figsize=(20, 5), rot=45)
    plt.title(f"Perbandingan Boxplot\n{kolom} terhadap Merk")

def data_list(data):

    df = data.iloc[371:374,:]

    mobil = df["Car"].to_list()
    tenaga = df["Tenaga"].to_list()
    efisiensi = df["Efisiensi"].to_list()
    rekomendasi = df["Rekomendasi"].to_list()

    for var in ['mobil', 'tenaga', 'efisiensi', 'rekomendasi']:
        print(f"{var.ljust(11)} = {eval(var)}")

    return mobil, tenaga, efisiensi, rekomendasi