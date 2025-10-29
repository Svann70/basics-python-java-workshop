# Program Klasifikasi Usia
print("Program Klasifikasi Usia")
print ("========================")
# 1. TODO: Baca input dari pengguna
usia = int(input("Masukkan Usia : "))
# 2. TODO Tentukan kategori berdasarkan usia
if usia >= 65 and usia <= 120 :
    print('Kamu Termasuk Kategori Manula')
elif 56 <= usia <= 65 :
    print('Kamu Termasuk Kategori Lansia Akhir')
elif 46 <= usia <= 55 :
    print('Kamu Termasuk Kategori Lansia Awal')
elif 36 <= usia <= 45 :
    print('Kamu Termasuk Kategori Dewasa Akhir')
elif 26 <= usia <= 35 :
    print('Kamu Termasuk Kategori Dewasa Awal')
elif 17 <= usia <= 25 :
    print('Kamu Termasuk Kategori Remaja Akhir')
elif 12 <= usia <= 16 :
    print('Kamu Termasuk Kategori Remaja Awal')
elif 5 <= usia <= 11 :
    print('Kamu Termasuk Kategori Kanak-kanak')
elif 0 <= usia <= 5 :
    print('Kamu Termasuk Kategori Balita')
else:
    print ('Kamu Sepuh')
