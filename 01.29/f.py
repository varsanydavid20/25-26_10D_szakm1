"""# Filmhossz átalakító program
def perc_to_ora_perc(percek):
    ora = percek // 60
    perc_maradek = percek % 60
    return f"{ora} óra {perc_maradek} perc"

print("Add meg három film címét és hosszát percben!\n")

filmek = []
for i in range(3):
    cim = input(f"{i+1}. film címe: ")
    hossz = int(input(f"{i+1}. film hossza (perc): "))
    filmek.append((cim, hossz))

print("\nFilmek hosszának átalakítása:")
for cim, hossz in filmek:
    atalakitas = perc_to_ora_perc(hossz)
    print(f"{cim}: {hossz} perc = {atalakitas}")

"""