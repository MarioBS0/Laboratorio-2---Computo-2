import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('coldplay.csv') #Cuando descargue el CSV le puse ese nombre

# Seleccionar solo la canción más popular de cada álbum
cancion = df.loc[df.groupby('album_name')['popularity'].idxmax()]

popularidad = cancion['popularity']  # Extraer la popularidad de las canciones
nombre = cancion['name']  # Extraer el nombre dela cancion

# Para generar el gráfico circular con los valores y etiquetas especificados.
plt.pie(popularidad, labels=nombre, autopct='%1.1f%%', startangle=90)

# Esto asegura que el gráfico no se vea alargado.
plt.axis('equal')
plt.title('Canciones mas populares de Coldplay ')
plt.show()

