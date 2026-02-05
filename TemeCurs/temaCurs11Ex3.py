import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----- 1. Generare date -----

np.random.seed(2)

n_ratings = 10000

user_ids = np.random.randint(1, 1001, n_ratings)
film_ids = np.random.randint(1, 101, n_ratings)
ratings = np.random.randint(1, 6, n_ratings)

filme = pd.DataFrame({
    "ID Utilizator": user_ids,
    "ID Film": film_ids,
    "Rating": ratings
})

# ----- 2. Procesare date -----

medie_film = filme.groupby("ID Film")["Rating"].mean()
top5 = medie_film.sort_values(ascending=False).head(5)

stats_filme = filme.groupby("ID Film").agg(
    Nr_Evaluari=("Rating", "count"),
    Rating_Mediu=("Rating", "mean")
)

filme_proaste = stats_filme[(stats_filme["Nr_Evaluari"] > 50) & (stats_filme["Rating_Mediu"] < 3.5)]

print("Top 5 filme dupa rating mediu:")
print(top5)

print("\nFilme cu peste 50 evaluari si rating mediu sub 3.5:")
print(filme_proaste)

# ----- 3. Vizualizari -----

# histograma ratinguri
plt.figure()
plt.hist(filme["Rating"], bins=5)
plt.title("Distributia ratingurilor")
plt.show()

# bar chart top 5 filme
plt.figure()
top5.plot(kind="bar", title="Top 5 filme dupa rating mediu")
plt.show()

# scatter nr evaluari vs rating mediu
plt.figure()
plt.scatter(stats_filme["Nr_Evaluari"], stats_filme["Rating_Mediu"])
plt.title("Nr evaluari vs rating mediu")
plt.xlabel("Numar evaluari")
plt.ylabel("Rating mediu")
plt.show()
