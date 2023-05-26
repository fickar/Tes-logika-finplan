bilangan = [2, 3, 4, 6]
bilangan.sort()

count = 1
for bil in bilangan:
    bil = bil + 1
    if(bil == bilangan[count]):
        pass
    else:
        print('Bilangan yang hilang adalah : ', bil)
        break
    count+=1    