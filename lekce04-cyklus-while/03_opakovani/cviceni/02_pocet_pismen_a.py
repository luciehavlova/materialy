# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.

slovo = input("Zadej slovo: ")
pocet = 0
for znak in slovo:
    if znak == "a":
        pocet = pocet + 1
print("Písmeno a se objevuje ve slově:", pocet, "krát")

 