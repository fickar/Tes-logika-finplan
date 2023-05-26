bilangan = []
def tampilkan_kelipatan_tiga(n):
    for i in range(1, n+1):
        kelipatan = i * 3
        bilangan.append(kelipatan)
    return bilangan

n = int(input("Masukkan banyaknya kelipatan tiga yang ingin ditampilkan: "))
hasil = tampilkan_kelipatan_tiga(n)

newBilangan = []
for bil in hasil:
    if bil % 3 == 0 and bil % 7 == 0:
        bil = bil
        bil = 'z'
    newBilangan.append(bil)

print(f"Kelipatan tiga pertama sebanyak {n} adalah: {newBilangan}")


