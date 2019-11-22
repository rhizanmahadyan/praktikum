#Latihan1
#Akses List 5 Element Angka

list_angka = [40, 50, 60, 70, 80]
print(list_angka)
print(list_angka[2])
print(list_angka[1:4])
print(list_angka[-1])

#Ubah Element List

list_angka[3] = 45
print(list_angka[3])
list_angka[3:4] = 48, 55
print(list_angka[3:5])

#Tambah ELement List

list_tambahAngka = list_angka[0:2]
print(list_tambahAngka)
list_tambahAngka.append(25)
print(list_tambahAngka)
list_tambahAngka.extend([35, 45, 55])
print(list_tambahAngka)
list_gabungkanAngka = list_angka + list_tambahAngka
print(list_gabungkanAngka)
