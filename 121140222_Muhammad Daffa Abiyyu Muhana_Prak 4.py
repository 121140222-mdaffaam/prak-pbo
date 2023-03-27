class Karyawan:
    def __init__(self, nama_karyawan, gaji_karyawan, jabatan_karyawan):
        self.nama_karyawan = nama_karyawan
        self.gaji_karyawan = gaji_karyawan
        self.jabatan_karyawan = jabatan_karyawan

    def lihat_info(self):
        print(f"{self.nama_karyawan} memiliki jabatan {self.jabatan_karyawan} dengan gaji Rp {self.gaji_karyawan}")

class Manajer(Karyawan):
    def __init__(self, nama_karyawan, gaji_karyawan, jabatan_karyawan, nama_cabang):
        super().__init__(nama_karyawan, gaji_karyawan, jabatan_karyawan)
        self.nama_cabang = nama_cabang

    def lihat_info(self):
        super().lihat_info()

class Teknisi(Karyawan):
    def __init__(self, nama_karyawan, gaji_karyawan, jabatan_karyawan):
        super().__init__(nama_karyawan, gaji_karyawan, jabatan_karyawan)

    def maintenance(self, nama_cabang):
        print(f"{self.nama_karyawan} sedang melakukan maintenance (perbaikan) di cabang {nama_cabang}")
    
    def lihat_info(self):
        super().lihat_info()

Malika = Karyawan("Malika", "5000000", "staff")
Adrian = Manajer("Adrian", "12000000", "Tanjung Karang", "staff")
Syarif = Teknisi("Syarif","7000000", "staff")
# Duck typing untuk fungsi lihat_info()
for karyawan in Malika, Adrian, Syarif:
    karyawan.lihat_info()
# Hanya ada pada kelas Teknisi
Syarif.maintenance("Tanjung Karang")


