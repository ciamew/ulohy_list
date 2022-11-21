import random
zoz = []
for i in range(10):
    zoz.append(random.randrange(0,100))
print(zoz)

def findmaximum(index:int)->int:
    #premena vo vnutri funkcie == likalna premena
    maxhodnota = zoz[index]
    maxindex = index
    for i in range(index,(len(zoz))):
        if zoz[i] > maxhodnota:
            maxhodnota = zoz[i]
            maxindex = i
    return maxindex
print(findmaximum(0))

for i in range(0,len(zoz)):
    maxindex = findmaximum(i)
    zoz[i],zoz[maxindex] = zoz[maxindex],zoz[i]
print(zoz)
