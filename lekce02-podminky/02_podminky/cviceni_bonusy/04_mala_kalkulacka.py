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
    print("Výsledek:", cislo1 + cislo2)
elif znamenko == "-":
    print("Výsledek:", cislo1 - cislo2)
elif znamenko == "*":
    print("Výsledek:", cislo1 * cislo2)
elif znamenko == "/":
    if cislo2 == 0:
        print("Nulou nelze dělit!")
    else:
     print("Výsledek:", cislo1 / cislo2)
else:
    print("Neznámé znaménko.")
    

