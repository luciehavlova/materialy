# Bonus 2 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Spočítej cyklem součet všech sudých čísel od 1 do 100 a vypiš ho.

soucet = 0
for cislo in range(1, 101):
    if cislo % 2 == 0:
        soucet = soucet + cislo
print(soucet)

"""
for c in range(2, 101, 2):
    soucet = soucet + c
print(soucet)
"""


