# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.

kolik = 0

while True:
    heslo = input("Zadej heslo: ")
    kolik = kolik + 1
    if heslo == "pyladies":
        print("Vítejte!")
        break
    if kolik == 3:
        print("Zablokováno")
        break
    print("Špatně, zkus to znovu.!!!")


