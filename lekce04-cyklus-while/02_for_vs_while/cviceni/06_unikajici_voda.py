# Cvičení 6 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# V nádrži je 45 litrů vody a každou minutu z ní uteče 3 litry.
#    Po každé minutě vypiš, kolik vody zbývá, a nakonec vypiš,
#    po kolika minutách je nádrž prázdná.

nadrz = 45
minuty = 0

while nadrz > 0:
    nadrz = nadrz - 3
    minuty = minuty + 1
    print("Po", minuty, "minutách zbývá", nadrz, "litrů vody.")
print("Nádrž je prázdná po", minuty, "minutách")


