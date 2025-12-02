"""szam =int(input("szám:"))
osszeg=szam

while(osszeg<=100):
    szam=int(input("szám:"))
    osszeg+=szam
    """

import random

gondolt = random.randint(1, 100)
print("Gondoltam egy számra 1 és 100 között. Találd ki melyik az!")
tipp = int(input("tipp: "))

while(tipp != gondolt):
    if(tipp < gondolt):
        print("Nagyobb számra gondoltam.")
    else:
        print("Kisebb számra gondoltam.")
    tipp = int(input("tipp: "))
    db+=1

print("Gratulálok" ,db, "próbálkozásból eltaláltad .")