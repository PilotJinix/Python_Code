import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

df = pd.read_csv("botak.csv",sep=',',header=0, index_col=False)
df.loc[df['is_menikah'] == 0, 'is_keturunan'] = 0

cats = ['jenis_kelamin', 'pekerjaan', 'sampo', 'pendidikan', 'provinsi']
nums = ['umur', 'gaji', 'is_menikah', 'is_keturunan', 'berat', 'tinggi', 'is_merokok', 'botak_prob']
header = ['jenis_kelamin', 'pekerjaan', 'sampo', 'pendidikan', 'provinsi','umur', 'gaji', 'is_menikah', 'is_keturunan', 'berat', 'tinggi', 'is_merokok', 'botak_prob']

df[nums].describe()
df[cats].describe()

# sns.boxplot(x="variable", y="value", data=pd.melt(df))
# plt.show()
# sns.set(style='ticks', color_codes=True)
# sns.pairplot(df)

path = sys.path
# Tempat save
# print(path[0])
# Tempat save
df.to_excel(fr'{path[0]}\data.xlsx', index=False)