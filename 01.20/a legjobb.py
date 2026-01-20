
"""
1.
jelszo=input("Kérek egy jelszót: ")
    if len(jelszo)<8:
        print("A jelszó túl rövid.")
    else:
        vankkis=False
        vannagyis=False
        vanszam=False
        for karakter in jelszo:
            if karakter.islower():
                vankkis=True
            elif karakter.isupper():
                vannagyis=True
            elif karakter.isdigit():
                vanszam=True
        if vankkis and vannagyis and vanszam:
            print("A jelszo eros.")"""

"""2. név=input("Kérek egy nevet: ")
helyesnév=név.title()
print("A helyes név:",helyesnév)
"""
