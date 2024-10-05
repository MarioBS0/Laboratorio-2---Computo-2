import pandas as pd  
import matplotlib.pyplot as plt  

# Cargar el dataset
df = pd.read_csv('juegos_Switch.csv') #Cuando descargue el CSV le puse ese nombre

# Ordenar los videojuegos por el numero de copias vendidas en orden descendente
ventas = df.sort_values(by='copies_sold', ascending=False).head(5) # Obtener solo los 5 mas vendidos (lo hice asi porque no sabia como hacer que se viera mejor ya que eran muchos datos)

# Convertir las ventas a millones
ventas['ventas_en_milliones'] = ventas['copies_sold'] / 1000000

# Crear la grafica de barras
x = ventas.plot.bar(x='title',  # El eje X (nombre del videojuego)
                           y='ventas_en_milliones',  # el eje Y (ventas)
                          rot=45)  # para que los nombres esten a 45 grados para que se vea mejor

# Añadir un titulo y etiquetas a la grafica
plt.title('5 Videojuegos más vendidos de Switch') 
plt.ylabel('Copias vendidas en Millones')
plt.tight_layout()  # Ajustar la grafica para que no se corten las etiquetas
plt.show()  
