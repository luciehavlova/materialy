# Cvičení 1 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Analýza věty. Uživatel zadá větu. Projdi ji znak po znaku a vypiš
#    počet znaků, počet samohlásek, počet mezer a počet slov ve větě.
#    (Počet slov = počet mezer + 1.)

veta = input("Zadej větu: ")
samohlasky = 0
mezery = 0

for pismeno in veta:
    if pismeno in "aeiou":
        samohlasky = samohlasky + 1
    if pismeno == " ":
        mezery = mezery + 1

print("Počet znaků ve větě:", len(veta))
print("Samohlásky: ", samohlasky)
print("Mezery: ", mezery)
print("Slova: ", mezery + 1)











             
