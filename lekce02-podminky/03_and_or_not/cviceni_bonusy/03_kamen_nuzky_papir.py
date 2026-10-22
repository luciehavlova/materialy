# Bonus 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".

hrac1 = input("Zadej svůj tah (kámen/nůžky/papír): ")
hrac2 = input("Zadej svůj tah (kámen/nůžky/papír): ")

if hrac1 == hrac2:
    print("Remíza.")
elif (hrac1 == "kámen" and hrac2 == "nůžky") or (hrac1 == "nůžky" and hrac2 == "papír") or (hrac1 == "papír" and hrac2 == "kámen"):
    print("Vyhrál hráč číslo 1.")
else:
    print("Vyhrál hráč číslo 2.")








