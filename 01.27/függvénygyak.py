
dolgozat = input("max pontszám:")
nev = input("név:") 
pontszam = input("elért pontszám:")

def szazalek(dolgozat, pontszam):
    return (int(pontszam) / int(dolgozat)) * 100
def elérés(szazalék):
    if szazalék >= 40:
        return "átment"
    else:
        return "nem ment át"
szazalék = szazalek(dolgozat, pontszam)
print(nev, round(szazalék,2), "%", elérés(szazalék))