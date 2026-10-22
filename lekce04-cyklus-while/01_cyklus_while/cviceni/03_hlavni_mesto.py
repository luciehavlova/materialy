# Cvičení 3 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".

mesto = input("Zadej hlavní město České republiky: ")

while mesto != "Praha":
    print("Špatně")
    mesto = input("Zadej znovu hlavní město ČR: ")
print("Správně")

