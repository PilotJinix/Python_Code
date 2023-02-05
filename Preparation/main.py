import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ## MEET ke 5 tanggal 12-06-2022
#
# a1d = np.square(np.arange(10))
# print(a1d)
#
# a2d = np.square(np.arange(15)).reshape((5,3))
# print(a2d)
#
# df_marks = pd.DataFrame({
#     'name' : ['apple', 'banana', 'orange', 'mango'],
#     'calories': [68, 74, 77, 78]
# })
#
# print(df_marks)
#
# for index, row in df_marks.iterrows():
#   print(index, ': ', row['name'], 'has ', row['calories'], ' calories.')
#
# for index, row in df_marks.iterrows():
#   print(type(index), type(row))
#
# for ind in df_marks.index:
#   print(df_marks['name'][ind], df_marks['calories'][ind])
#
#
# #Iterating over rows using loc funtion
# for i in range(len(df_marks)):
#   print(df_marks.loc[i, "name"], df_marks.loc[i, "calories"])
#
#
# #Iterating over rows using loc function
# for i in range(len(df_marks)):
#   print(df_marks.iloc[i, 0], df_marks.iloc[i, 1])
#
#
# data = pd.read_csv('nba.csv')
#
# print(data.head()) #print 5 baris pertama data


# <---Fake Data for Plotting---->
# Median ages
ages = ['25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']

# Median Microbiologist Salaries by Age
mib_salary = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Median Pharmacist Salaries by Age
pharma_salary = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

# Median Cader Salaries by Age
bcs_salary = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]

fig, ax = plt.subplots()
ax.plot(ages, mib_salary, label='micro')
ax.plot(ages, pharma_salary, label='micro')
ax.plot(ages, bcs_salary, label='bcs')
plt.legend(loc='best')
plt.xlabel('da')
plt.ylabel('qwerty')
plt.title('data')
plt.show()



