zoznam = ['jozo','kubo','mato','cau','ako','autobus','hajde','no','aninie','cc']
samohlaska = 'aeiyou'
zoznamn = []
pocets = 0

for i in range(0,len(zoznam)):
    for x in range(len(zoznam[i])):
        if ((zoznam[i])[x]) in samohlaska:
            pocets += 1
    zoznamn.append(pocets)
    pocets = 0
print(zoznamn)
