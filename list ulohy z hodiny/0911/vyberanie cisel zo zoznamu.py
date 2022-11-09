#napis zoznam random 10 cisel
import random
zoz = []
for i in range(10):
    zoz.append(random.randrange(0,21))
print(zoz) #(*zoz) vypisuje dane znaky z listu bez ciarok a zatvoriek

#vyber najvacie cislo, kt. sa nachadza v zozname
#vypis na kt. pozici sa nachadza toto cislo
maximum = zoz[0]
poziciamax = 0
for i in range(1, len(zoz)):
    if zoz[i] > maximum:
        maximum = zoz[i]
        poziciamax = i+1  #+1 preto lebo za prvu poziciu mi rata 0
print("Najvacsie cislo v zozname je:", maximum)
print("Pozicia najvacsieho cisla je:", poziciamax)

# vypis sucet parnych a neparnych cisel v zozname
sucetp = 0
sucetnp = 0
for i in range(0, (len(zoz))):
    if zoz[i] % 2 == 0:
        sucetp += zoz[i]
    else:
        sucetnp += zoz[i]
print("Sucet parnych cisel je:", sucetp)
print("Sucet neparnych cisel je:", sucetnp)

#vypis pocet parnych cisel na parnych poziciach
pocetpp = 0
for i in range(0, (len(zoz)),2): # 0 preto lebo ako prva parna pozicia je hned prve cislo v zozname, 2 lebo idem po parnych poziciach cize 2
    if zoz[i] % 2 == 0:
        pocetpp += 1
    else:
        pocetpp + 0
print("Pocet parnych cisel na parnych poziciach je:", pocetpp)

#vypis pocet parnych cisel na neparnych poziciach
pocetpn = 0
for i in range(1, (len(zoz)),2):
    if zoz[i] % 2 == 0:
        pocetpn += 1
    else:
        pocetpn + 0
print("Pocet parnych cisel na neparnych poziciach je:", pocetpn)

#vypis pocet neparnych cisel na parnych poziciach
pocetnp = 0
for i in range(0, (len(zoz)),2):
    if zoz[i] % 2 != 0:
        pocetnp += 1
    else:
        pocetnp + 0
print("Pocet neparnych cisel na parnych poziciach je:", pocetnp)

#vypis pocet parnych cisel na neparnych poziciach
pocetnp = 0
for i in range(1, (len(zoz)),2):
    if zoz[i] % 2 == 0:
        pocetnp += 1
    else:
        pocetnp + 0
print("Pocet parnych cisel na neparnych poziciach je:", pocetnp)