# Control flow adalah konsep dalam pemrograman yang mengacu pada urutan eksekusi pernyataan atau instruksi dalam sebuah program. Ini menentukan bagaimana komputer akan menjalankan berbagai bagian program berdasarkan kondisi-kondisi tertentu. Control flow memungkinkan untuk membuat alur logika yang berbeda tergantung pada situasi yang ada saat program dijalankan.

"""
data = ["Fikri","Fahri","Salsa"]
nama = input("Masukkan Nama: ")
if nama in data:
    print("Halo Anggota COCONUT")
else:
    print("Bukan Anggota COCONUT")
"""

"""
angka = int(input("Masukkan Angka: "))    
if angka <= 5 and angka >=0:
    print(f"{angka} lebih kecil atau sama dengan 5")
elif angka >=6:
    print(f"{angka}lebih besar dari 5")
else:
    print("Anda menginput kurang dari 0")
"""

"""
data = ["Fikri","Fahri","Salsa"]
nama = input("Masukkan Nama: ")

hasil = "Anggota Coconut" if nama in data else "Bukan Anggota"
print(hasil)
"""

"""
data = range(10)
for i in data: #range(10)
    if i == 5:
        continue
    print(i, end="\n")
"""

"""
data = range(10)
for i in data: #range(10)
    if i == 5:
        break
    print(i, end="\n")
"""

"""
data = ("nama", "usia","menikah")
for isi in data:
    print(isi)
"""

"""
data = {"nama":"fikri", "usia":20}
for isi in data:
    print(data [isi])
    """

"""
data = {"nama":"fikri", "usia":20}
for isi in data.values():
    print(isi)
    """

"""
nama = input("Masukkan Nama: ")

match nama:
    case "1":
        print("input 1")
    case "2":
        print("input 2")
    case "3":
        print("input 3")
"""

# try menghendel error
"""
angka = input("Masukkan hanya angka: ")
try:
    angka = int(angka)
    print("Angka",angka)
except:
    print("Anda menginput bukan angka")
    """

"""
rows = int(input("Masukkan jumlah baris: "))

for i in range(1, rows + 1):
  print("*" * i)
"""

"""
for i in range(6):
  print(" "* (6 - i), "* "* i)
"""
