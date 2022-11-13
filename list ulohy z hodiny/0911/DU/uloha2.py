# Napíš funkciu nakup(zoznam), ktorá spracuje nákupný zoznam a vráti jeho celkovú cenu.
# Vstupný zoznam obsahuje dvojice čísel v tvare [koľko, cena, koľko, cena, ...],
# ktorý pre každý nakúpený tovar označuje jeho množstvo (koľko) a jednotkovú cenu (cena).

zoznam = [3, 2.5, 0.5, 10, 1.2, 1.2]
def nakup(zoznam):
    celacena = 0
    for i in range(0,len(zoznam)):
        if i % 2 != 0:
            celacena += zoznam[i] * zoznam[i-1]
    return celacena
print(nakup(zoznam))




# nakup = [3, 2.5, 0.5, 10, 1.2, 1.2]
# def zoznam(nakup):
#     for i in range(3):
#         for pocet in range(0,(len(nakup)),2):
#             kolko = nakup[pocet]
#             print(kolko)
#
#         for cena in range(1,(len(nakup)),2):
#             kolko2 = nakup[cena]
#             print(kolko2)
#
#         for i in range(3):
#             celacena = kolko*kolko2
#             print(celacena)
# print(zoznam(nakup))