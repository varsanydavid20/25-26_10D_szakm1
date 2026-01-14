szo = input("Adj meg egy szót: ")
maganhangzok = "aáeéiíoóöőuúüű"
db = 0
for karakter in szo:
    if karakter.lower() in maganhangzok:
        db += 1
print(f"A szóban {db} magánhangzó van.")