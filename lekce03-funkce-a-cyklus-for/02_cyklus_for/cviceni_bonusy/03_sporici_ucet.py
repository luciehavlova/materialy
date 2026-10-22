# Bonus 3 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počáteční částku na spořicím účtu. Úrok je 5 % ročně.
#     Spočítej cyklem, kolik na účtu bude po deseti letech
#     (každý rok se částka vynásobí 1.05), a výsledek vypiš.

ucet = int(input("Zadej částku na spořícím účtu: "))

for rok in range(10):
    ucet = ucet * 1.05
print(ucet)
print(round(ucet, 2))


