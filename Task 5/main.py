import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

set1 = {
    'customer_id' : ['hXgxB', 'UZ2T4', '9Tjgq', 'CQ-0D', '9q0sp'],
    'nama_customer' : ['Usyi Usada', 'Gaduh Prakasa', 'Mariadi Pangestu', 'Ella Nurdiyanti', 'Putu Prabowo'],
    'no_seri_motor' : ['12cae392-f465-11ec-b939-0242ac120002', '12cae568-f465-11ec-b939-0242ac120002', '12caeb94-f465-11ec-b939-0242ac120002', '12caece8-f465-11ec-b939-0242ac120002', '12caeec8-f465-11ec-b939-0242ac120002'],
    'alamat_customer' : ['Jl Gorontalo 9, Dki Jakarta', 'Jl Pasar Suci, Jawa Barat', 'Jl Krekot Dlm Bl H/9 D, Dki Jakarta', 'Jl Tj Morawa Km 13/8, Sumatera Utara', 'Jl Letjen Suprapto Graha Cempaka Mas Bl K/6, Dki Jakarta'],
}
set2 = {
    'no_seri_motor' : ['12cae392-f465-11ec-b939-0242ac120002', '12cae568-f465-11ec-b939-0242ac120002', '12caeb94-f465-11ec-b939-0242ac120002', '12caece8-f465-11ec-b939-0242ac120002', '12caeec8-f465-11ec-b939-0242ac120002'],
    'jenis_motor' : ['Honda', 'Yamaha', 'Kawasaki', 'Suzuki', 'Yadea'],
    'harga_motor' : [15000000, 21000000, 19000000, 25000000, 20000000],
    'jenis_pembayaran_motor' : ['Cash', 'Kredit', 'Kredit', 'Cash', 'Cash']
}
directory1 = pd.DataFrame(set1)
directory2 = pd.DataFrame(set2)

join = directory1.merge(directory2, how='left', on=['no_seri_motor'])
join = join.sort_values(by='harga_motor', ascending=False)
path = sys.path
# Tempat save
# print(path[0])
# Tempat save
# join.to_csv(fr'{path[0]}\data.csv', index=False)

data_csv = 'Telco-Customer-Churn - Telco-Customer-Churn.csv'
file = pd.read_csv(data_csv, sep=',', header=0, index_col=False)
print(file.isnull().sum())
# print(file.info())
# print(file.dtypes)
changetype = {
    "gender" : 'category',
    "SeniorCitizen" : bool,
    "MonthlyCharges" : float,
    "TotalCharges" : float
}
file = file.astype(changetype)
# file.to_excel(fr'{path[0]}\new.xlsx')

print(file[file['customerID'].duplicated(keep=False)])
file['TotalCharges']=file['TotalCharges'].fillna(file['TotalCharges'].median())
print(file.isnull().sum())

sns.boxplot(file['TotalCharges'])
# plt.show()

print(file.describe(include="all"))

# print(file.iloc[0,1,100].loc['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn'])
# print(file.loc[file.iloc[[0,1], :], ['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']])

print(file.loc[[0,10,100], ['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']])


data_presentase = file.groupby(['Churn'])[['customerID']].count().reset_index()
data_presentase['Presentage'] = data_presentase['customerID'] / data_presentase['customerID'].sum() * 100
# print(data_presentase)

behavior_data = file.groupby(['Contract','Churn']).size().unstack()
colors  = ['#FAC900','#009E3C']

result = (behavior_data.T*100.0 / behavior_data.T.sum()).T.plot(kind='bar',width = 0.3,stacked = True,rot = 0,figsize = (12,7),color = colors)

plt.ylabel('Persentase Jumlah Customer',horizontalalignment="center",fontstyle = "normal",fontsize = "large", fontfamily = "sans-serif")
plt.xlabel('Contract',horizontalalignment="center", fontstyle = "normal", fontsize = "large", fontfamily = "sans-serif")
plt.title('Churn data by Contract ', horizontalalignment="center", fontstyle = "normal",fontsize = "22", fontfamily = "sans-serif")
plt.legend(loc='upper right', fontsize = "medium")
plt.xticks(rotation=0, horizontalalignment="center")
plt.yticks(rotation=0, horizontalalignment="right")
result.yaxis.set_major_formatter(mtick.PercentFormatter())
for index in result.patches:
    width, height = index.get_width(), index.get_height()
    x, y = index.get_xy()
    result.text(x+width/2, y+height/2, '{:.1f}%'.format(height), horizontalalignment='center', verticalalignment='center')
result.autoscale(enable=False, axis='both', tight=False)

# plt.show()

numberoffacility = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
fig, axes = plt.subplots(nrows=2, ncols=3,figsize=(15, 12))
for i, item in enumerate(numberoffacility):
    if i < 2:
        ax = file[item].value_counts().plot(kind='bar', ax=axes[i, 0],rot=0, color='#f3babc')
        ax.set_title(item)

    elif i >= 2 and i < 4:
        ax = file[item].value_counts().plot(kind='bar', ax=axes[i - 2, 1],rot=0, color='#9b9c9a')
        ax.set_title(item)

    elif i < 6:
        ax = file[item].value_counts().plot(kind='bar', ax=axes[i - 4, 2], rot=0,color='#ec838a')
        ax.set_title(item)

# plt.show()

filter_data = file.query("tenure<30 and MonthlyCharges>60 and Contract=='Month-to-month'")
inverse_data = file.query("tenure>30 and MonthlyCharges<60 and Contract!='Month-to-month'")
print('==============================')
print(filter_data)
print(filter_data['MonthlyCharges'].mean())
print(inverse_data)
