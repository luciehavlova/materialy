# Cvičení 8 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Zboží stojí 1000 Kč bez DPH. Na jeden řádek vypiš cenu bez DPH
#    i s DPH (21 %). Použij dva printy – první nech řádek pokračovat,
#    druhý ho dokonči.
cena = 1000

dph = (cena * 21 / 100) + cena
# print(dph)

print("Cena bez DPH", cena, end= " a ")
print("Cena s DPH", dph)