# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

from Tarea1 import df_Movies

# 2. Leer el archivo CSV
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_Movies = pd.read_csv(file_path)

#3.Promedio de valoración del tomatómetro y la audiencia o publico
print(df_Movies['tomatometer_rating'].mean())

print(df_Movies['audience_rating'].mean())

#Se crea la nueva columna que resta la valoracion de tomatometro y la audiencia
df_Movies['rating_diff'] = df_Movies['audience_rating'] - df_Movies['tomatometer_rating']


# 13. Histograma de las diferencias de valoración
plt.figure(figsize=(10, 6))
plt.hist(df_Movies['rating_diff'], bins=30, edgecolor='black', color='#66CDAA')
plt.xlabel('Diferencia (Audiencia - Críticos)')
plt.ylabel('Número de películas')
plt.title('Distribución de la diferencia entre audiencia y críticos')
plt.show()