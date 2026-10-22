# Cvičení 3 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává čísla tak dlouho, dokud nezadá 0. Nakonec vypiš
#    jejich součet, kolik jich bylo a jejich průměr zaokrouhlený
#    na jedno desetinné místo. (Nápověda: round(cislo, 1))


cislo = int(input("Zadej číslo (0 = konec): "))
soucet = 0
kolikrat = 0

while cislo != 0:
    soucet = soucet + cislo 
    kolikrat = kolikrat + 1
    cislo = int(input("Zadej číslo (0 = konec): "))

if kolikrat == 0:
    print("Nezadal jsi žádné číslo")
else:
    print("Součet zadaných čísel je: ", soucet)
    print("Průměr zadaných čísel je: ", round(soucet / kolikrat, 1))
    print("Počet zadaných čísel je: ", kolikrat)
                





