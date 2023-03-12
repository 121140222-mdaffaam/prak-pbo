import random

class Kotak:
    def __init__(self):
        self.isi = 'bom' if random.random() < 0.2 else 'kosong'
        self.status = 'belum dibuka'
        self.jumlah_bom = None
    
    def tampilkan(self):
        if self.status == 'belum dibuka':
            return '?'
        elif self.isi == 'bom':
            return 'x'
        else:
            return 'o'
    
    def buka_kotak(self):
        self.status = 'sudah dibuka'


dimensi = int(input("Masukkan dimensi area: "))
    
area = [[Kotak() for j in range(dimensi)] for i in range(dimensi)]
    
for i in range(dimensi):
    for j in range(dimensi):
        if area[i][j].isi == 'kosong':
            area[i][j].jumlah_bom = 0
            for k in range(max(i-1, 0), min(i+2, dimensi)):
                for l in range(max(j-1, 0), min(j+2, dimensi)):
                    if area[k][l].isi == 'bom':
                        area[i][j].jumlah_bom += 1
    
for i in range(dimensi):
    for j in range(dimensi):
        print(area[i][j].tampilkan(), end=' ')
    print()
    
selesai = False
sisa_kotak = dimensi * dimensi
while not selesai:
    nomor_kotak = int(input("Masukkan nomor kotak yang ingin dibuka (1-{}): ".format(dimensi*dimensi)))
    i = (nomor_kotak - 1) // dimensi
    j = (nomor_kotak - 1) % dimensi
        
    if area[i][j].isi == 'bom':
        print("Game over! Kotak tersebut berisi bom.")
        selesai = True
    else:
        area[i][j].buka_kotak()
        sisa_kotak -= 1
            
        if sisa_kotak == sum([1 for i in range(dimensi) for j in range(dimensi) if area[i][j].isi == 'bom']):
            print("Selamat! Anda telah memenangkan game.")
            selesai = True
        
        for i in range(dimensi):
            for j in range(dimensi):
                if area[i][j].status == 'belum dibuka':
                    print('?', end=' ')
                else:
                    print(area[i][j].tampilkan(), end=' ')
            print()
        print("Selamat! kotak tersebut tidak berisi bom.")