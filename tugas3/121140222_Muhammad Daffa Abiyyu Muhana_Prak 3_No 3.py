class Mobil:
    def __init__(self, merk, tahun, harga):
        self.merk = merk # atribut public
        self.tahun = tahun # atribut public
        self._harga = harga # atribut protected
        self.__warna = 'merah' # atribut private
        
    def get_harga(self):
        return self._harga
    
    def set_harga(self, harga):
        self._harga = harga
        
    def get_warna(self):
        return self.__warna
    
    def set_warna(self, warna):
        self.__warna = warna
        
    def info_mobil(self):
        print(f"Merk: {self.merk}")
        print(f"Tahun: {self.tahun}")
        print(f"Harga: {self._harga}")
        print(f"Warna: {self.__warna}")
        
mobil1 = Mobil('Toyota', 2022, 350000000)

# akses atribut public
print(mobil1.merk) # output: Toyota
print(mobil1.tahun) # output: 2022

# akses atribut protected
print(mobil1.get_harga()) # output: 350000000

# mengubah atribut protected
mobil1.set_harga(300000000)
print(mobil1.get_harga()) # output: 300000000

# akses atribut private
print(mobil1.get_warna()) # output: merah

# mengubah atribut private
mobil1.set_warna('biru') # tidak berubah karena akses gagal

# panggil metode untuk menampilkan info mobil
print("\nSetelah diubah")
print("--------------")
mobil1.info_mobil()
