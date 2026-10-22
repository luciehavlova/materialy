# Cvičení 4 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.

cislo = int(input("Zadej číslo (0 = konec): "))
soucet = 0

while cislo != 0:
    soucet = soucet + cislo 
    cislo = int(input("Zadej číslo (0 = konec): "))
print("Součet zadaných čísel je: ", soucet)

 
