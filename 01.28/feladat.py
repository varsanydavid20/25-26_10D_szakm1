"""import random

lista = [random.randint(0,9) for _ in range(10)]
print("Eredeti lista:", lista)

paratlanok_szama = sum(1 for x in lista if x % 2 == 1)
print("Páratlan számok száma:", paratlanok_szama)

unique_lista = list(set(lista))
print("Ismétlődők eltávolítva:", unique_lista)

minden_szam = set(range(10))  
hianyak = sorted(minden_szam - set(lista))

print("Hiányzó számok 0-9 között:", hianyak if hianyak else "Nincs hiányzó szám")


"""
import random


def feltolt(Lista):
    for i in range(10):
        Lista.append(random.randint(0,9))
        return Lista

def paratlan():
    None

def ismetlodes():
    None

def hianyzo():
    None

