# Napíš funkciu sucin(zoznam), ktorá vráti (return) súčin prvkov zoznamu
# (zoznam obsahuje len čísla).
# Ak je zoznam prázdny, funkcia vráti 1.

# zoznam = [2, 3, 5, 7, 11]
# zoznam = list(range(1, 11))
# zoznam = ([2] * 20)

def sucin(zoznam):
    sucinprv = 1
    for i in range(0,len(zoznam)):
        sucinprv = sucinprv * zoznam[i]
    return sucinprv
print(sucin(zoznam))