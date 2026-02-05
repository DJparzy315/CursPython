import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----- 1. Generare date -----

np.random.seed(0)

zile = pd.date_range(start="2024-01-01", periods=365)

temperatura = np.random.uniform(5, 35, 365)
umiditate = np.random.uniform(30, 90, 365)
vant = np.random.uniform(0, 20, 365)

meteo = pd.DataFrame({
    "Data": zile,
    "Temperatura": temperatura,
    "Umiditate": umiditate,
    "Viteza Vantului": vant
})

# ----- 2. Procesare date -----

# calcul temperatura resimtita
meteo["Temperatura Resimtita"] = meteo["Temperatura"] - 0.7 * (meteo["Umiditate"] / 100)

# ziua cu max si min temperatura resimtita
zi_max = meteo.loc[meteo["Temperatura Resimtita"].idxmax()]
zi_min = meteo.loc[meteo["Temperatura Resimtita"].idxmin()]

print("Ziua cu temperatura resimtita maxima:")
print(zi_max[["Data", "Temperatura Resimtita"]])

print("\nZiua cu temperatura resimtita minima:")
print(zi_min[["Data", "Temperatura Resimtita"]])

# ----- 3. Vizualizari -----

# grafic linie temperatura vs temperatura resimtita
plt.figure()
plt.plot(meteo["Data"], meteo["Temperatura"], label="Temperatura")
plt.plot(meteo["Data"], meteo["Temperatura Resimtita"], label="Temp Resimtita")
plt.legend()
plt.title("Temperatura vs Temperatura Resimtita")
plt.show()

# temperatura medie lunara
meteo["Luna"] = meteo["Data"].dt.month
medie_lunara = meteo.groupby("Luna")["Temperatura"].mean()

plt.figure()
medie_lunara.plot(kind="bar", title="Temperatura medie lunara")
plt.show()
