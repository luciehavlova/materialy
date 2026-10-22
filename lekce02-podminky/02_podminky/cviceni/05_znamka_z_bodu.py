# Cvičení 5 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na počet bodů z testu (0 až 100) a vypiš známku:
#    90 a víc → 1, 75 a víc → 2, 60 a víc → 3, 40 a víc → 4,
#    jinak → 5.

body = int(input("Zadej počet bodů z testu: "))

if body >= 90:
    print("Známka: 1")
elif body >= 75:
    print("Známka: 2")
elif body >= 60:
    print("Známka: 3")
elif body >= 40:
    print("Známka: 4")
else:
    print("Známka: 5")

    
