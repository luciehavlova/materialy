# Cvičení 2 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# Vypiš účtenku tak, aby ceny byly pod sebou: název zarovnaný doleva
#    na dvanáct míst, cenu doprava na osm míst se dvěma desetinnými
#    místy. Na konec přidej řádek se součtem.
#
#    Když je součet vyšší než 150 Kč, přidej ještě řádek se slevou
#    deset procent a řádek s cenou po slevě.

polozka1 = "káva"
cena1 = 59
polozka2 = "dort"
cena2 = 84.5
polozka3 = "čaj"
cena3 = 45

def radek(nazev, castka):
    print(f"{nazev:12}{castka:8.2f}")

radek(polozka1, cena1)
radek(polozka2, cena2)
radek(polozka3, cena3)

soucet = cena1 + cena2 + cena3
radek("Součet:", soucet)

if soucet > 150:
    sleva = soucet * 10 / 100
    radek("Sleva:", sleva)
    radek("Cena:", soucet - sleva)
    
# pro zarovnání všech údajů voláme funkci radek a 
# nikoliv print, který funguje, ale data nejsou zarována do tabulky
