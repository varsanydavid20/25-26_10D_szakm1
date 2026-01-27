
def kivon(szam1, szam2):
    return szam1 - szam2

def osszead(szam1, szam2):
    return szam1 + szam2

def szoroz(szam1, szam2):
    return szam1 * szam2

def oszt(szam1, szam2):
    if szam2 != 0:
        return szam1 / szam2
    else:
        return "Hiba: nullával nem lehet osztani!"  

szam1 = int(input("Kérem az elsőszámot: "))
szam2 = int(input("Kérem a második számot: "))
muvjel=input("Kérem a művelet jelét:")

if muvjel=='+':
    print("Az eredmény:",osszead(szam1, szam2))
elif muvjel=='-':
    print("Az eredmény:",kivon(szam1, szam2))
elif muvjel=='*':
    print("Az eredmény:",szoroz(szam1, szam2))
elif muvjel=='/':
    print("Az eredmény:",oszt(szam1, szam2))
else:
    print("Hibás műveleti jel!")