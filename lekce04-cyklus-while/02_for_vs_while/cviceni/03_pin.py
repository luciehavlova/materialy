# Cvičení 3 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Ptej se na PIN tak dlouho, dokud uživatel nezadá "1234".
#    Pak vypiš "Odemčeno!".

pin = input("Zadej PIN ke své kartě: ")

while pin != "1234":
    print("Chybný PIN")
    pin = input("Zadej PIN: ")
print("Odemčeno!")

    
