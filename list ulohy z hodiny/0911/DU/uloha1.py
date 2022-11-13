# Napíš funkciu vypis_typy(zoznam), ktorá vypíše všetky prvky zoznamu a ku každému vypíše informáciu o jeho type:
# ak je to int alebo float, tak vypíše 'číslo'; ak je to str, tak vypíše 'reťazec';
# inak všetky ostatné typy vypíše ako 'iný typ'.

zoznam = [12, 'x', None, 3.14, [], range(5), '123']
def vypis_typy(zoznam):
    for i in range(7): #cislo v range sa meni podla toho kolko prvkov je v zozname
        prvok = (zoznam[i])
        # print(prvok)
        if type(prvok) == int or type(prvok) == float:
            print(zoznam[i], "- cislo")
        elif type(prvok) == str:
            print(zoznam[i], "- retazec")
        else:
            print(zoznam[i], "- iny typ")
print(vypis_typy(zoznam))





# zoznam = [12, 'x', None, 3.14, [], range(5), '123']
# x = -1
# for i in range(7):
#     x += 1
#     prvok = (zoznam[x])
#     # print(prvok)
#     if type(prvok) == int or type(prvok) == float:
#         print(zoznam[x], "- cislo")
#     elif type(prvok) == str:
#         print(zoznam[x], "- retazec")
#     else:
#         print(zoznam[x], "- iny typ")
