#napis funkciu ktora sa bude volat jozo, bude mat jeden parameter zoznam,
#funkcia vracia true ak je v zozname viac parnych, ak je viac neparnych vracia false

#zoznam = [10,13,55,12,82,9,6]
zoznam = [5,3,7,9,13,11,45,2]
def jozo(zoznam):
    parne = 0
    neparne = 0
    for i in range(0,len(zoznam)):
        if zoznam[i] % 2 == 0:
            parne += 1
        else:
            neparne += 1
    if parne > neparne:
        stav = True
    elif parne == neparne:
        stav = "obidve rovnake"
    else:
        stav = False
    return stav
print(jozo(zoznam))