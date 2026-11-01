# ---------------------------------------------
#  Užitečné metody řetězců
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

veta = "Ahoj PyLadies!"

print(veta.upper())                      # AHOJ PYLADIES!
print(veta.lower())                      # ahoj pyladies!
print(veta.count("a"))                   # 1 - kolikrát je znak v řetězci
print("Ahoj Adame".lower().count("a"))   # nejdříve řetězec převedena na malá písmena a pak spočítá kolikrát je "a" v řetězci
print(veta.replace("Ahoj", "Nazdar"))    # Nazdar PyLadies! - nahrazení za Ahoj

# count("a") našlo jedno "a" – to v PyLadies. Velké "A" ze slova Ahoj
# je pro Python jiný znak.

print("anna nováková".title())           # Anna Nováková


# Metoda strip() odstraní mezery na krajích. Ve výpisu nejsou mezery
# vidět, hranaté závorky je ukážou:
odpoved = "  ano  "
print(f"[{odpoved}]")                    # [  ano  ]
print(f"[{odpoved.strip()}]")            # [ano]


# Metod je mnohem víc. Ve VS Code napiš tečku za řetězec nebo za proměnnou
# a editor ti nabídne seznam. Pamatovat si je nemusíš – ty nejpoužívanější
# jsou i v taháku k téhle lekci.

# cvičení v hodině:

def zadej_email():
    return input("Zadej e-mail: ").lower()

zadej_email()

