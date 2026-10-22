# Bonus 2 – Vstup od uživatelky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.

castka = int(input("Zadej celkovu částku: "))
lidi = int(input("Zadej celkový počet lidí: "))

print("Každý zaplatí celkovu částku", castka // lidi, "Kč a celkem zbyde", castka % lidi, "Kč.")

