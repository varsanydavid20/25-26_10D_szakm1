"""1.
szo= input("Add meg egy szót: ")
print(szo == szo[::-1])
"""

"""2.
szo = input("Adj meg egy szót: ")

eredmeny = ""
for i in range(len(szo)):
    if (i + 1) % 3 != 0:   # minden 3. betű kimarad
        eredmeny += szo[i]

print("Eredmény:", eredmeny)
"""

"""3. 
szo1 = input("Add meg az első szót: ")
szo2 = input("Add meg a második szót: ")

# Megkeressük a rövidebb és hosszabb szót
if len(szo1) <= len(szo2):
    rovidebb = szo1
    hosszabb = szo2
else:
    rovidebb = szo2
    hosszabb = szo1

# Eldöntés
if rovidebb in hosszabb:
    print("A rövidebb szó szerepel a hosszabbikban.")
else:
    print("A rövidebb szó nem szerepel a hosszabbikban.")
"""

"""4. szoveg = input("Adj meg egy szöveget: ")

db = 0
for betu in szoveg:
    if betu == "s":
        db += 1

print("Az 's' betűk száma:", db)"""