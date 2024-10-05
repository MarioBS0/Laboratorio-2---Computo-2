import pandas as pd 
import matplotlib.pyplot as plt

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('marvel_taquilla.csv') #Cuando descargue el CSV le puse ese nombre

# Convertir la columna 'release_date' a tipo datetime y extraer el anio
df['release_date'] = pd.to_datetime(df['release_date'])  
df['anio'] = df['release_date'].dt.year  # Extraer el anio

# Convertir la columna 'worldwide_box_office' a tipo numerico, eliminando comas
df['worldwide_box_office'] = df['worldwide_box_office'].replace(',', '', regex=True).astype(float)

# Agrupar por anio y sumar las taquillas
taquilla = df.groupby('anio')['worldwide_box_office'].sum().reset_index()

# Crear un grafico de lineas
plt.plot(taquilla['anio'], taquilla['worldwide_box_office'])

# Añadir titulo y etiquetas
plt.title('Taquilla Mundial de Películas de Marvel')  # Titulo de la grafica
plt.xlabel('Año de Lanzamiento')  # Etiqueta del eje X
plt.ylabel('Taquilla Mundial (en miles de millones)')  # Etiqueta del eje y
plt.show() 

