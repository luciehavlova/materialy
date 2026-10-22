# Bonus 1 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.

utrata = float(input("Zadejte celkovou útratu: "))
lidi = float(input("Zadej počet lidí: "))

cena = utrata / lidi
print(round(cena, 2))


