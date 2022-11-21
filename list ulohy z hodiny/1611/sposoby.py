zoz = []
for i in range(10):
    zoz.append(input("zadaj mi",i,"-ty prvok zoznamu"))

# 1.sposob
print(*zoz) #bez zatvoriek s medzerami
print(zoz) #so zatvorkami, su ciarky

for i in range(10): #i je vzdy int, index toho prvku!!
    print(zoz[i])

for prvok in zoz:
    print(prvok,type(prvok)) #prvok je takeho typu aky je ulozeny v zozname

for index, hodnota in enumerate(zoz):
    print(index)
    print(hodnota)