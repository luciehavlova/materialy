# Bonus 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Malá kalkulačka.
#     Zeptej se na dvě čísla a na znaménko (+, -, *, /).
#     Podle znaménka vypiš výsledek správné operace.
#     Bonus v bonusu: ošetři dělení nulou vlastní hláškou.

cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))
znamenko = input("Zadej požadované znaménko (+, -, *, /): ")

if znamenko == "+":
    print("Součet čísel je: ", cislo1+cislo2)
elif znamenko == "-":
    print("Odečet dvou čísel je: ", cislo1-cislo2)
elif znamenko == "*":
    print("Součin dvou čísel je: ", cislo1*cislo2)
elif znamenko == "/":
    if cislo2 == 0:
        print("Nulou nejde dělit!!!")
    else:
        print("Dělení dvou čísel je: ", cislo1/cislo2)
else:
    print("Neznámé znaménko!!!")
