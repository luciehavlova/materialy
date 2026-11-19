# ---------------------------------------------
#  Index a výřez: jako u řetězců
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

hoste = ["Anna", "Petra", "Jana", "Eva", "Marie", "Lucie"]


# Index a výřez fungují stejně jako u řetězců z lekce 6. Index počítá
# od nuly, záporný index od konce:
#
# (Index i výřez v seznamu ukazuje obrázek seznam_index_a_vyrez.png.)

print(hoste[0])         # Anna
print(hoste[2])         # Jana
print(hoste[-1])        # Lucie


# Výřez vrátí nový seznam. Číslo před dvojtečkou se do něj počítá,
# číslo za dvojtečkou už ne:
prvni_dva = hoste[0:2]
print(prvni_dva)        # ['Anna', 'Petra']

# Původní seznam přitom zůstane celý:
print(hoste)    # ['Anna', 'Petra', 'Jana', 'Eva', 'Marie', 'Lucie']

# Začátek a konec můžeš vynechat. Fungují i záporná čísla:
print(hoste[:2])        # ['Anna', 'Petra']
print(hoste[4:])        # ['Marie', 'Lucie']
print(hoste[-2:])       # ['Marie', 'Lucie']

# Index je hodnota jako každá jiná, takže ho můžeš uložit do proměnné:
posledni = len(hoste) - 1
print(hoste[posledni])  # Lucie

for host in hoste:
    print("Zvu Vás na svůj Vánoční večírek", host)

print("První pozvaný host, byl/byla", hoste[0])

# přepište jako for cyklus s range:
pocet_hostu = len(hoste)
for host in range(pocet_hostu):
    print("Zveme Vás na Vánoční večírek", hoste[host]) # pokud necháme jen host, vrací číslo, nebo-li index

blacklist = ["Hegerova", "Vlk"]

# prichozi = input("Jak se jmenujes?: ")

"""
for host in hoste:
    if prichozi == host:
        print("Pojď dál", prichozi)
"""

# možnost porovnání pomocí in:
def kontrola(prichozi, hoste, blacklist):
    if prichozi in hoste:
        print("Pojď dál", prichozi)
    elif prichozi in blacklist:
        print("Zmiz než si tě všimne Karel!!!")
    else:
        print("Nejsi zván")
# kontrola(prichozi, hoste, blacklist)


def pozvi(jmeno, hoste):
    hoste.append(jmeno)
pozvi("Vojta", hoste)
print(hoste)
hoste[5:5] = ["Tom", "Jerry"]
print(hoste)
hoste[0] = "Martina"
print(hoste)

# Šest hostů má indexy 0 až 5. Index 6 už v seznamu není:
# print(hoste[6])         # IndexError: list index out of range

# split, run, join (split funguje na řetězce a ne na seznamy)
# inicialy:

organizator = "Karel Gott"  
print(organizator)

print(organizator.split())
inicialy = organizator.split()[0][0] + organizator.split()[1][0]
print(inicialy)

inicialy = ""
for slovo in organizator.split():
    inicialy = inicialy + slovo[0]
print(inicialy)

inicialy = []
for slovo in organizator.split():
    inicialy.append(slovo[0])
print(inicialy)
print("-".join(inicialy))


def odeber_hosta(jmeno, hoste):
    hoste.remove(jmeno)

odeber_hosta("Vojta", hoste)
print(hoste)

fronta = ["Vojta", "Petra", "Oslík", "Shrek"]
fronta.pop(0) # smažeme první prvek v seznamu, tj. Vojta
# Pošleme na kontrolu do funkce kontroly:
kontrola(fronta.pop(0), hoste, blacklist)
print(hoste)

hoste.sort() #  seřazení seznamu dle abecedy
print(hoste)