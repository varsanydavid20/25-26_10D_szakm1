"""
import math
# Bekérjük az a, b, c értékeket
a = float(input("Add meg a értékét: "))
b = float(input("Add meg b értékét: "))
c = float(input("Add meg c értékét: "))
# Számítjuk a diszkriminánst
D = b**2 - 4*a*c
# Ellenőrizzük a diszkrimináns értékét és kiírjuk az eredményt
if D < 0:
    print("Nincs valós gyök.")
elif D == 0:
    x = -b / (2 * a)
    print(f"Egy valós gyök: {x}")
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Két valós gyök: {x1} és {x2}")
"""


"""# Bekérjük az évet
ev = int(input("Add meg az évet: "))

# Ellenőrizzük a szökőév szabályát
if ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0):
    print(f"{ev} szökőév.")
else:
    print(f"{ev} nem szökőév.")"""


"""# Bekérjük az első számot
szam1 = float(input("Add meg az első számot: "))
# Bekérjük a műveleti jelet
muvelet = input("Add meg a műveleti jelet (+, -, *, /): ")
# Bekérjük a második számot
szam2 = float(input("Add meg a második számot: "))
# Számítjuk az eredményt a művelet alapján
if muvelet == '+':
    eredmeny = szam1 + szam2
    print(f"Eredmény: {szam1} + {szam2} = {eredmeny}")
elif muvelet == '-':
    eredmeny = szam1 - szam2
    print(f"Eredmény: {szam1} - {szam2} = {eredmeny}")
elif muvelet == '*':
    eredmeny = szam1 * szam2
    print(f"Eredmény: {szam1} * {szam2} = {eredmeny}")
elif muvelet == '/':
    if szam2 == 0:
        print("Hiba: Nullával nem lehet osztani!")
    else:
        eredmeny = szam1 / szam2
        print(f"Eredmény: {szam1} / {szam2} = {eredmeny}")
else:
    print("Hiba: Érvénytelen műveleti jel!")
"""

