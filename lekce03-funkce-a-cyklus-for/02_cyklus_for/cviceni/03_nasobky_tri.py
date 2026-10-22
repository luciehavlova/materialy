# Cvičení 3 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Cyklem vypiš násobky tří od 3 do 30 (tedy 3, 6, 9, ... až 30).

for cisla in range(3, 31, 3):
    print(cisla)

for cisla in range(3, 31):
    if cisla % 3 == 0:
        print(cisla)
        