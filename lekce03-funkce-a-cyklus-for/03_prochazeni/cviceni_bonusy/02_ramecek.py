# Bonus 2 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Rámeček. Uživatel zadá velikost N. Vnořenými cykly nakresli
#     čtverec N x N, kde okraj tvoří X a vnitřek je prázdný. Pro N=4:
#         X X X X
#         X     X
#         X     X
#         X X X X
#     Zamysli se: na kterém řádku a sloupci se kreslí X a kdy mezera?

velikost = int(input("Zadej velikost N: "))
for radek in range(velikost):
    for sloupec in range(velikost):
        if radek == 0 or radek == velikost - 1 or sloupec == 0 or sloupec == velikost - 1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()
       

    
