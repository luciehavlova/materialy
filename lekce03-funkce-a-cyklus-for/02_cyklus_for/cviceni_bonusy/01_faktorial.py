# Bonus 1 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá číslo N. Spočítej cyklem jeho faktoriál –
#     tedy 1 * 2 * 3 * ... * N – a výsledek vypiš.
#     (Faktoriál z 5 je 120.)

# Faktoriál čísla 0 znamená hodnotu 1 a pro každé přirozené číslo n jde o součin (násobek)
# všech přirozených čísel od jedné až do n (včetně), např. pro číslo 8 (1*2*3*4*5*6*7*8).

n = int(input("Zadej číslo N: "))

faktorial = 1
for cislo in range(1, n + 1):
    faktorial = faktorial * cislo
print(faktorial)


