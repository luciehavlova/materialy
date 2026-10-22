# Bonus 5 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Palindrom. Uživatel zadá slovo. Zjisti, jestli se čte stejně
#     zepředu i zezadu (třeba "kajak" nebo "radar").
#     Zamysli se, jak si slovo poskládáš pozpátku a jak obě verze porovnáš.

slovo = input("Zadej slovo: ")
obracene = ""

for pismena in slovo:
    obracene = pismena + obracene        # každé písmeno dáme PŘED dosavadní výsledek
if slovo == obracene:
    print("Je to palidrom.")
else:
    print("Není to palidrom.")



