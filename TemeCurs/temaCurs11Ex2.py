import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----- 1. Generare date -----

np.random.seed(1)

zile = pd.date_range(start="2023-01-01", periods=730)

schimbari = np.random.normal(0, 0.02, 730)  # procente zilnice
preturi = [100]

for i in range(1, 730):
    pret_nou = preturi[-1] * (1 + schimbari[i])
    preturi.append(pret_nou)

actiuni = pd.DataFrame({
    "Data": zile,
    "Schimbare Zilnica (%)": schimbari * 100,
    "Pret Inchidere": preturi
})

# ----- 2. Procesare date -----

actiuni["MA30"] = actiuni["Pret Inchidere"].rolling(window=30).mean()
actiuni["MA100"] = actiuni["Pret Inchidere"].rolling(window=100).mean()

# zile cand pretul e peste MA100
peste_ma100 = actiuni["Pret Inchidere"] > actiuni["MA100"]

# ----- 3. Vizualizari -----

plt.figure()
plt.plot(actiuni["Data"], actiuni["Pret Inchidere"], label="Pret")
plt.plot(actiuni["Data"], actiuni["MA30"], label="MA 30")
plt.plot(actiuni["Data"], actiuni["MA100"], label="MA 100")

# evidentiere zone peste MA100
plt.fill_between(actiuni["Data"], actiuni["Pret Inchidere"], actiuni["MA100"],
                 where=peste_ma100, alpha=0.3)

plt.legend()
plt.title("Pret actiune si medii mobile")
plt.show()
