import pandas as pd
import matplotlib.pyplot as plt

#Paises de menor tasa
df = pd.read_csv('AdolescentFertility.csv')
data = pd.DataFrame(df)
dataFiltered = data.sort_values(by=['2017'], ascending=True)[['Country Name', '2017']].head(10)
print(dataFiltered)

#Paises de mayor tasa
data = pd.DataFrame(df)
dataFiltered = data.sort_values(by=['2017'], ascending=False)[['Country Name', '2017']].head(10) 
print(dataFiltered)

#Promedio mundial
promedio1960 = df['1960'].mean()
promedio2017 = df['2017'].mean()
print(promedio1960) 
print(promedio2017)

#Menor tasa Nigeria y mayor tasa Corea del Norte
coreaN = df.iloc[149][4:].max() 
nigeria = df.iloc[189][4:].min()   
print(coreaN)
print(nigeria)

#Minimo y maximo Costa Rica
df_numeric = df.apply(pd.to_numeric, errors='coerce')
df_numeric = df_numeric.fillna(0)
CR_Max = df_numeric.iloc[92][4:].max()  
CR_Min = df_numeric.iloc[92][4:].min()  
CR_Min_column = df_numeric.iloc[92][4:].idxmin()
CR_Max_column = df_numeric.iloc[92][4:].idxmax()
print(f"El valor mínimo es {CR_Min} y se encuentra en la columna '{CR_Min_column}'")
print(f"El valor mínimo es {CR_Max} y se encuentra en la columna '{CR_Max_column}'")

#Grafico barras paises menos tasa
dataFiltered = data.sort_values(by=['2017'], ascending=True)[['Country Name', '2017']].head(10)

plt.figure(figsize=(10, 6))
plt.barh(dataFiltered['Country Name'], dataFiltered['2017'], color='skyblue')
plt.xlabel('Adolescent Fertility Rate (per 1000)')
plt.ylabel('Country Name')
plt.title('Top 10 paises con la fertilidad adolescente más baja en el 2017')
plt.gca().invert_yaxis()
plt.show()

#Grafico barras paises mas tasa
dataFiltered = data.sort_values(by=['2017'], ascending=False)[['Country Name', '2017']].head(10)

plt.figure(figsize=(10, 6))
plt.barh(dataFiltered['Country Name'], dataFiltered['2017'], color='skyblue')
plt.xlabel('Adolescent Fertility Rate (per 1000)')
plt.ylabel('Country Name')
plt.title('Top 10 paises con la fertilidad adolescente más alta en el 2017')
plt.gca().invert_yaxis()
plt.show()

#Grafico barras promedio de tasa
promedio1960 = df['1960'].mean()
promedio2017 = df['2017'].mean()

print("Promedio de fertilidad adolescente en 1960:", promedio1960)
print("Promedio de fertilidad adolescente en 2017:", promedio2017)

years = ['1960', '2017']
averages = [promedio1960, promedio2017]

plt.figure(figsize=(8, 5))
plt.bar(years, averages, color=['skyblue', 'lightgreen'])
plt.xlabel('Año')
plt.ylabel('Tasa promedio')
plt.title('Promedio de la tasa de fertilidad adolescente alrededor del mundo en 1960 y 2017')
plt.ylim(0, max(averages) * 1.1)

plt.show()

#Grafico barras max de coreaN y min de Nigeria
coreaN = df.iloc[149][4:].max()
nigeria = df.iloc[189][4:].min()

data = pd.DataFrame({'País': ['Corea del Norte', 'Nigeria'],
                     'Valor': [coreaN, nigeria]})

plt.figure(figsize=(8, 6))
plt.bar(data['País'], data['Valor'], color=['blue', 'green'])
plt.title('Comparación de la tasa de fertilidad adolescente mayor de Corea del Norte y la menor tasa Nigeria')
plt.xlabel('País')
plt.ylabel('Tasa')
plt.show()

#Grafico barras CR
data = pd.DataFrame({'Columna': [CR_Min_column, CR_Max_column],
                     'Valor': [CR_Min, CR_Max]})

plt.figure(figsize=(8, 6))
plt.bar(data['Columna'], data['Valor'], color=['red', 'orange'])
plt.title('Tasa mínima y máxima de fertilidad adolescente en Costa Rica')
plt.xlabel('Años')
plt.ylabel('Tasa')
plt.show()

#Grafico lineal CR
fila_92 = df_numeric.iloc[92][4:]

plt.plot(fila_92.index, fila_92.values)
plt.title('Tendencia de la tasa de fertilidad adolescente en Costa Rica desde 1960 hasta 2017')
plt.xlabel('Años')
plt.ylabel('Tasa')

years = df.columns[4:].astype(int)
plt.xticks(ticks=range(0, len(years), 5), labels=years[::5])

plt.tight_layout()
plt.show()
