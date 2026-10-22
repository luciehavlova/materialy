# Bonus 3 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Cíl a rozpočet. Uživatel zadá cenu tří položek. Vypiš nejlevnější
#     a nejdražší z nich a jestli se všechny tři vejdou do rozpočtu 1000 Kč.

polozka1 = int(input("Zadej cenu položky č. 1: "))
polozka2 = int(input("Zadej cenu položky č. 2: "))
polozka3 = int(input("Zadej cenu položky č. 3: "))

print(min(polozka1, polozka2, polozka3))
print(max(polozka1, polozka2, polozka3))

if polozka1 + polozka2 + polozka3 <= 1000:
    print("Vejde se do rozpočtu")
else:
    print("Překročili jste rozpočet")

    