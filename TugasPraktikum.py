# MengInisialisasikan
nama1=[]
nim1=[]
nilaitugas1=[]
nilaiuts1=[]
nilaiuas1=[]
akhir1=[]
respon = 'ya'
while respon =='ya':
    # Menginputkan Data
    nama = input("Nama  : ")
    kelas = input("NIM  : ")
    nilaitugas = int(input("Nilai Tugas    :"))
    nilaiuts = int(input("Nilai UTS :"))
    nilaiuas = int(input("Nilai UAS :"))
    akhir = int(nilaitugas)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100

    # Menambahkan Data 
    nama1.append(nama)
    nim1.append(kelas)
    nilaitugas1.append(nilaitugas)
    nilaiuts1.append(nilaiuts)
    nilaiuas1.append(nilaiuas)
    akhir1.append(akhir)
    
    respon = (input('Tambah data?(ya/tidak)'))
    if respon == 'tidak':

        # Mengesekusi/Menampilkan Data
        print("==========================================================================");
        print("| No |  Nama   |    NIM    | Tugas | UTS | UAS | Akhir |");
        print("==========================================================================");
        for i in range(len(nama1)):
            print("|", i+1 ,"|",  nama1[i]  ,"  |",  nim1[i]  ,"|",  nilaitugas1[i]  ,"|",  nilaiuts1[i]  ,"|",  nilaiuas1[i]  ,"|",  akhir1[i],"|")
       
