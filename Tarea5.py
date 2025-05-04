import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Rotten Tomatoes Movies.csv"
df_Movies = pd.read_csv(file_path)

# 1. Contar cuántas películas ha dirigido cada director
director_counts = df_Movies['directors'].value_counts().dropna()

# 2. Mostrar los 10 directores que aparecen con más frecuencia
top_10_directors = director_counts.head(10)
print("Los 10 directores más frecuentes:\n", top_10_directors)

top_10_director_names = top_10_directors.index.tolist()
df_top_10_directors = df_Movies[df_Movies['directors'].isin(top_10_director_names)].copy()
average_ratings_top_10_directors = df_top_10_directors.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)

print("Promedio de tomatometer_rating para los 10 directores más frecuentes:", average_ratings_top_10_directors)

# 4.gráfico de barras de 10 directores y su tomatometer_rating promedio
plt.figure(figsize=(12, 8))
plt.bar(average_ratings_top_10_directors.index, average_ratings_top_10_directors.values, color='skyblue')
plt.xlabel('Director')
plt.ylabel('Calificación Promedio (Tomatometer)')
plt.title('Calificación Promedio (Tomatometer) de los 10 Directores Más Frecuentes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()