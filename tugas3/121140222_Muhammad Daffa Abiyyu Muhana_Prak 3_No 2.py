class AkunBank:
    list_pelanggan = []
    
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.__class__.list_pelanggan.append(self)
        
    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print(f"Halo {self.__nama_pelanggan}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        
    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")
        
    def tarik_tunai(self, nominal):
        if nominal > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= nominal
            print("Saldo berhasil ditarik!")
    
    def transfer(self, nominal, no_rekening_tujuan):
        for pelanggan in self.__class__.list_pelanggan:
            if pelanggan.__no_pelanggan == no_rekening_tujuan:
                pelanggan.__jumlah_saldo += nominal
                self.__jumlah_saldo -= nominal
                print(f"Transfer Rp {nominal} ke {pelanggan.__nama_pelanggan} sukses!")
                return
        print("No rekening tujuan tidak dikenal! Kembali ke menu utama.")
    
    def main(self):
        while True:
            self.lihat_menu()
            pilihan = int(input("Masukkan nomor input: "))
            if pilihan == 1:
                self.lihat_saldo()
            elif pilihan == 2:
                nominal = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
                self.tarik_tunai(nominal)
            elif pilihan == 3:
                nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
                no_rekening_tujuan = int(input("Masukkan no rekening tujuan: "))
                self.transfer(nominal, no_rekening_tujuan)
            else:
                break
            print('')

Akun1 = AkunBank(1234, "M Daffa Abiyyu Muhana", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.main()
