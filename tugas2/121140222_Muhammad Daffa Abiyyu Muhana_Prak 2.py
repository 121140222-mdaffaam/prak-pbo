class Manusia:

    def __init__(self, nama, NIM, Angkatan, gender, Matkul, Kelas_asal):
        self.nama = nama
        self.NIM = NIM
        self.Angkatan = Angkatan
        self.gender = gender
        self.Matkul = Matkul
        self.Kelas_asal = Kelas_asal

    def Kelas(self, kelas_sekarang):
        print(f"Kelas asal : {self.Kelas_asal}")
        print(f"Kelas praktikum : {kelas_sekarang}")


Manusia1 = Manusia("M Daffa Abiyyu Muhana", 121140222, 2021, "Laki-laki", "PBO", "RD")
print("Nama :", Manusia1.nama)
print("NIM :", Manusia1.NIM)
print("Mata kuliah :", Manusia1.Matkul)
Manusia1.Kelas("RB")
print("Angkatan :", Manusia1.Angkatan)
print("Jenis kelamin :", Manusia1.gender)