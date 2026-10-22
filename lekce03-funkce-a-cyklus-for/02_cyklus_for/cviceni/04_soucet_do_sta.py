# Cvičení 4 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Spočítej součet všech čísel od 1 do 100 pomocí cyklu for
#    (ne funkcí sum) a výsledek vypiš.

print(sum(range(1, 101)))

soucet = 0
for cisla in range(1, 101):
    soucet = soucet + cisla
print(soucet)

