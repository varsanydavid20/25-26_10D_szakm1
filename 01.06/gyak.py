import locale

locale.setlocale(locale.LC_ALL, 'hu_HU.UTF-8')

lista = ["Attila","Vilmos","Áron","Tamara","Erika","Tamás",100,2,1]

lista.sort()
print(lista)
lista.sort(key=locale.strxfrm)
print(lista)