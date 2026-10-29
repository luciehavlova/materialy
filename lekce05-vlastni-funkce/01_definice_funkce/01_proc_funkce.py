# ---------------------------------------------
#  Proč vlastní funkce
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# Funkce používáš od první lekce. Dřív jsme jim říkali vestavěné funkce –
# Python je má připravené a napsal je někdo jiný:
#
#   print("Ahoj")       vypíše text
#   input("Jméno: ")    počká na odpověď
#   len("Ahoj")         spočítá znaky
#   round(3.14159, 2)   zaokrouhlí
#   randrange(1, 7)     hodí kostkou
#
# Pokaždé je to stejné: napíšeš jméno funkce, do závorek pošleš hodnoty,
# se kterými má pracovat, a ona odvede svoji práci. Kdo ji napsal a co
# je uvnitř, řešit nemusíš.
#
# Na všechno ale hotová funkce být nemůže – co budeš zrovna potřebovat,
# dopředu nikdo netuší. Od téhle lekce si funkce píšeš sama – třeba
# takovou, která zkontroluje, jestli je heslo dost dlouhé.
#
# Nejdřív se podíváme, jak taková kontrola vypadá bez ní.
# Heslo bereme jako dost dlouhé, když má aspoň 8 znaků:

moje_heslo = "kolo"
if len(moje_heslo) < 8:
    print(moje_heslo, "– moc krátké")
else:
    print(moje_heslo, "– dost dlouhé")

moje_heslo = "pyladies2026"
if len(moje_heslo) < 8:
    print(moje_heslo, "– moc krátké")
else:
    print(moje_heslo, "– dost dlouhé")

moje_heslo = "abc"
if len(moje_heslo) < 8:
    print(moje_heslo, "– moc krátké")
else:
    print(moje_heslo, "– dost dlouhé")


# Stejné čtyři řádky třikrát. Až se hranice změní z 8 na 10,
# musíme to opravit na třech místech a na žádné zapomenout.


# Kontrolu si proto pojmenujeme a napíšeme jenom jednou:
def zkontroluj_heslo(heslo):
    if len(heslo) < 8:
        print(heslo, "– moc krátké")
    else:
        print(heslo, "– dost dlouhé")


# Samotné def ještě nic nevypíše. Funkce se spustí, až když ji zavoláme:
zkontroluj_heslo("kolo")
zkontroluj_heslo("pyladies2026")
zkontroluj_heslo("abc")


# Na pořadí výpisů je ten rozdíl vidět. Python si při čtení definice funkci
# jenom zapamatuje a dovnitř se zatím nepodívá:
print("před definicí")


def pozdrav():
    print("uvnitř funkce")


print("po definici")
pozdrav()
print("po zavolání")


# Takhle se definice čte:
#   def              = klíčové slovo (definuju funkci)
#   zkontroluj_heslo = jméno, které si volíš sama
#   (heslo)          = parametr, se kterým funkce pracuje
#   :                = dvojtečka na konci řádku
#   odsazení         = odsazené řádky jsou tělo funkce
#
# (Definici a zavolání ukazuje obrázek definice_funkce.png.)


def vypis_cisla_do_max_hodnoty(jmeno_volani, max_hodnota, ukaz_caru):
    for cislo in range(1, max_hodnota):
        print(jmeno_volani, ":", cislo)
    if ukaz_caru:
        print("*"*30)
    
vypis_cisla_do_max_hodnoty("Volani A", 10, True)
vypis_cisla_do_max_hodnoty("Volani B", 20, True)
vypis_cisla_do_max_hodnoty("Volani C", 30, False)


def cena_mhd(vek):
    print("Počítám cenu lístku pro věk", vek)

    if vek < 6:
        # print("Cena je 0") - je nahrazeno printem níže, return jen vrací částku do funkce, aby 
        # s částkou mohl dále pracovat nížeji
        return 0
    elif vek < 18:
        # print("Cena je 24")
        return 24
    elif vek < 65:
        # print("Cena je 39")
        return 39
    else:
        # print("Cena je 0")
        return 0

zustatek_uctu = 100
cena_jizdenky = cena_mhd(7)   # přiřazením do proměnné voláme funkci 
print("Výsledná cena je: ", cena_jizdenky)

zustatek_uctu = zustatek_uctu - cena_jizdenky
print(zustatek_uctu)

