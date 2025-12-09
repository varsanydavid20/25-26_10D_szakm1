"""Lszamok=[1,2,3,4,5]
for i in range(len(Lszamok)):
     print(Lszamok[i])

     print(Lszamok)
    """


import random

lszamok=[]
for i in range(10):
    szam=random.randint(1,100)
    lszamok.append(random.randint(1,100))
print(lszamok)
print("első szám:",lszamok[0])
print("utolsó szám:",lszamok[-1])