# Bonus 2 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Největší ze tří.
#     Máš tři čísla. Zjisti a vypiš to největší z nich.
a = 12
b = 25
c = 8

if a > b and a > c:
    print("Největší číslo je číslo", a)
elif b > a and b > c:
    print("Největší číslo je číslo", b)
else:
    print("Největší číslo je číslo", c)

# druhé řešení pomocí vnořených podmínek:
if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)