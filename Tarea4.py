import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Rotten Tomatoes Movies.csv"
df_Movies = pd.read_csv(file_path)

# copia del DataFrame para no modificar el original
df_genres = df_Movies.copy()

df_genres_exploded = df_genres['genre'].str.split(', ').explode().to_frame(name='genre')

df_genres_exploded = df_genres_exploded.merge(df_Movies[['audience_rating']], left_index=True, right_index=True)

average_ratings_by_genre = df_genres_exploded.groupby('genre')['audience_rating'].mean()

top_10_genres = average_ratings_by_genre.sort_values(ascending=False).head(10)

# diagrama de pastel
plt.figure(figsize=(10, 10))
plt.pie(top_10_genres, labels=top_10_genres.index, startangle=140)
plt.title('Top 10 géneros con mejor promedio de valoración de audiencia')
plt.axis('equal')
plt.show()