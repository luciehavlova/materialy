# Bonus 1 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Trojúhelník z hvězdiček. Uživatel zadá výšku a ty vypiš
#     trojúhelník, kde první řádek má jednu hvězdičku, druhý dvě atd.:
#     *
#     **
#     ***

vyska = int(input("Zadej výšku trojúhelníku: "))
for radek in range(1, vyska + 1):  # vyska + 1 - zajistí, že se nevynechá ani to poslední číslo
    print("*" * radek)



# čtverec:
velikost = int(input("Zadej velikost čtverce: "))

for radek in range(velikost):
    # Vytiskne řádek plný hvězdiček (s mezerami pro lepší vzhled čtverce)
    print("* " * velikost)

obdelnik1 = int(input("Zadej výšku obdelníku: "))
obdelnik2 = int(input("Zadej šíři obdelníku: "))
# for radek in range(obdelnik1):
    # print("* " * obdelnik2)

# pomoci vnořených cyklů:
for radek in range(obdelnik1):
    for sloupec in range(obdelnik2):
        print("*", end=" ")
    print()




    

