import random
zoz = []
for i in range(5):
    zoz.append(random.randrange(0,100))
print(zoz)

def bubblesort(zoz):
    prvok = len(zoz)
    while prvok > 0:
        for y in range(len(zoz)-1):
            if zoz[y] > zoz[y+1]:
                zoz[y], zoz[y+1] = zoz[y+1], zoz[y]
        prvok = prvok - 1
    return zoz
print(bubblesort(zoz))