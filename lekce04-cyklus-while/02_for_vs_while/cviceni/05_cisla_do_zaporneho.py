# Cvičení 5 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Načítej od uživatele čísla tak dlouho, dokud nezadá záporné číslo.
#    Pak vypiš, kolik čísel stihl zadat.


cislo = int(input("Zadej číslo: "))
kolik = 0

while cislo >= 0: 
    kolik = kolik + 1
    cislo = int(input("Zadej číslo: "))

print("Počet zadaných čísel před tím záporným:", kolik)

