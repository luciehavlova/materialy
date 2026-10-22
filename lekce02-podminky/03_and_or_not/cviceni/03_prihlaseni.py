# Cvičení 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Přihlášení. Správné jméno je "anna" a správné heslo je "tajne".
#    Zeptej se na jméno i heslo a vypiš "Vítej!", jen když sedí obojí.
#    Jinak vypiš "Špatné údaje.".

jmeno = "anna"
heslo = "tajne"

jmeno_zadani = input("Zadej jmeno: ")
heslo_zadani = input("Zadej heslo: ")

if jmeno_zadani == jmeno and heslo_zadani == heslo:
    print("Vítej!")
else:
    print("Špatné údaje.")

    