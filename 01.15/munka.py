"""1.
szo = input("Adj meg egy szót: ")
if szo == szo[::-1]:
    print("A szó palindrom.")
else:
    print("A szó nem palindrom.")
"""

szoveg=input("Adj meg egy szöveget: ")

szam="123456789"
Lszamok=[]
for karakter in szoveg:
    if (karakter in szam):
        Lszamok.append(int(karakter))
