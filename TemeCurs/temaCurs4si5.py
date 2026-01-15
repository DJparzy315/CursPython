# Dictionar cu preturile produselor
preturi = {
    "mere": 1.0,
    "banane": 0.5,
    "portocale": 0.8,
    "mango": 1.5
}

# Dictionar cu stocul initial
stoc = {
    "mere": 10,
    "banane": 20,
    "portocale": 15,
    "mango": 5
}

# Lista de tupluri cu vanzarile din timpul zilei
vanzari = [
    ("mere", 4),
    ("banane", 6),
    ("portocale", 10),
    ("mango", 2)
]

venit_total = 0.0

# Procesarea vanzarilor
for produs, cantitate in vanzari:
    # Calculam venitul pentru fiecare produs vandut
    venit_total += preturi[produs] * cantitate
    # Actualizam stocul
    stoc[produs] -= cantitate

# Set pentru produsele ce trebuie realimentate
realimentare = set()

# Verificam stocurile ramase
for produs, cantitate in stoc.items():
    if cantitate < 5:
        realimentare.add(produs)

# Afisarea raportului final
print(f"Venit total: {venit_total} RON")
print("Stocuri ramase:")
for produs, cantitate in stoc.items():
    print(f"  - {produs}: {cantitate}")

print("Produse ce necesita realimentare:")
for produs in realimentare:
    print(f"  - {produs}")
