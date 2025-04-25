#  1.Carga del Dataset

# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# 2. Leer el archivo CSV
file_path = "./Data/Rotten Tomatoes Movies.csv"
df_Movies = pd.read_csv(file_path)

#Muestra las primeras 5 filas del dataframe
print(df_Movies.head())

#verirficar los tipos de datos de cada columna
df_Movies.info()

#Convertir columnas in_theaters_date a datetime
df_Movies['in_theaters_date'] = pd.to_datetime(df_Movies['in_theaters_date'])

#Verificar nuevamente los tipos de datos
print(df_Movies.dtypes)


# 7. Mostrar si hubo valores no convertidos (NaT)
missing_dates = df_Movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")
