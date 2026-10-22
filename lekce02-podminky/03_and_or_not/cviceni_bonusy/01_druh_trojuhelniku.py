# Bonus 1 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Druh trojúhelníku. Máš tři strany. Urči a vypiš, jaký to je
#     trojúhelník:
#       - "rovnostranný", když jsou všechny tři strany stejné,
#       - "rovnoramenný", když jsou aspoň dvě strany stejné,
#       - "různostranný", když jsou všechny strany různé.
a = 5
b = 5
c = 8

if a == b and b == c and a == c:
    print("Rovnostranný trojúhelník")
elif a == b or b == c or a == c:
    print("Rovnoramenný troúhelník")
else:
    print("Různostranný trojúhelník")








"""
if a == b and b == c and a == c:
    print("Trojúhelník je rovnostranný.")
elif a == b or b == c or a == c:
    print("Trojúhleník je rovnoramenný.")
else:
    print("Trojúhelník je různostranný.")
"""

