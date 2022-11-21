import random
zoz = []
for i in range(10):
    zoz.append(random.randrange(0,100))
print(zoz)

def findminimum(index:int)->int:
    minhodnota = zoz[index]
    minindex = index
    for i in range(index,(len(zoz))):
        if zoz[i] < minhodnota:
            minhodnota = zoz[i]
            minindex = i
    return minindex
print(findminimum(0))

for i in range(0,len(zoz)):
    minindex = findminimum(i)
    zoz[i], zoz[minindex] = zoz[minindex], zoz[i]
print(zoz)