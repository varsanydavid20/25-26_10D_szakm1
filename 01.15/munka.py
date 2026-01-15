
szoveg = input("Adj meg egy szöveget: ")

osszeg = 0
aktualis_szam = ""

for karakter in szoveg:
    if karakter.isdigit():
        aktualis_szam += karakter
    else:
        if aktualis_szam != "":
            osszeg += int(aktualis_szam)
            aktualis_szam = ""

# ha a szöveg végén szám van
if aktualis_szam != "":
    osszeg += int(aktualis_szam)

print("A szövegben található számok összege:", osszeg)
