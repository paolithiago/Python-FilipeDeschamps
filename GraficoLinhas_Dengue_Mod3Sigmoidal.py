#https://colab.research.google.com/drive/1wqUZyVogLcz4fwD2cEhkGYUiIZaMu6rR#scrollTo=MhliMHZa_FyA

import pandas as pd
import matplotlib.pyplot as plt                     # IMPORTA BIBLIOTECA MATPLOTLIB


df = pd.read_csv('https://raw.githubusercontent.com/carlosfab/dsnp2/master/datasets/dengue-dataset.csv')
print(df.head())                               #cinco primeiras linhas, porem precismos ajustar a dat pois estao como strings como babixo
print(df.dtypes)                               #Veja que a coluna dara esta como objeto e nao como data
df['data']=pd.to_datetime(df['data'])             #Converte a coluna data de objeto para date time
print("-------------------\n")
print(df.dtypes)                               #Veja que a coluna dara esta como objeto e nao como data

df['data'] = pd.to_datetime(df['data'])
plt.title('Casos Dengue')
plt.xlabel("Data")
plt.ylabel('Casos Confirmados')
plt.plot('data','casos-confirmados', data = df)
plt.show()
