# Cvičení 3 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Statistika čísel. Uživatel zadá, kolik čísel bude zadávat, a pak
#    ta čísla postupně napíše. V jednom průchodu cyklem spočítej a vypiš
#    jejich součet, průměr, největší a nejmenší číslo.
#    Nepoužívej funkce sum, max ani min – spočítej vše sama cyklem.

pocet = int(input("Kolik čísel zadáš: "))
prvni = int(input("Zadej první číslo: "))
soucet = prvni
nejvetsi = prvni
nejmensi = prvni

for cislo in range(pocet - 1):
    dalsi = int(input("Zadej další číslo: "))
    soucet = soucet + dalsi
    if dalsi > nejvetsi:
        nejvetsi = dalsi
    if dalsi < nejmensi:
        nejmensi = dalsi
print("Součet čísel je: ", soucet)
print("Průměr čísel je: ", soucet / pocet)
print("Největší číslo je: ", nejvetsi)
print("Nejmenší číslo je: ", nejmensi)

