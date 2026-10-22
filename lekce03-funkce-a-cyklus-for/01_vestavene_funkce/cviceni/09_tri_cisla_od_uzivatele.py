# Cvičení 9 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se uživatele na tři čísla (klidně i záporná) a vypiš,
#    jak velké je to největší z nich bez ohledu na znaménko.
#    Např. z čísel -20, 5 a 12 je největší velikost 20.

cislo1 = int(input("Zadej prvé číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))
cislo3 = int(input("Zadej třetí číslo: "))

print(max(abs(cislo1), abs(cislo2), abs(cislo3)))
