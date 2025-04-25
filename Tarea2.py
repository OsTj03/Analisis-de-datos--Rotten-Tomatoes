# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# 2. Leer el archivo CSV
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_Movies = pd.read_csv(file_path)

# 3. muestra cuantas peliculas hay en total Mostrar en consola
print(len(df_Movies))

# 4. muestra Cuenta cuántas películas pertenecen a cada categoría
print(df_Movies['tomatometer_status'].value_counts())

#5. gráfico circular para mostrar la proporción de cada tomatometer_status.

plt.pie(df_Movies['tomatometer_status'].value_counts(), labels = df_Movies['tomatometer_status'].value_counts().index, startangle=140)
plt.title('Distribución de clasificacion por la crítica')
plt.show()