#variabel adalah suatu nama yang digunakan untuk menampung nilai
"""
nama ="fikri"
usia = 12
tinggi_badan = 160.5
menikah = False

biodata = [nama, usia, tinggi_badan, menikah] #bisa dimanipulasi
biodataTupple = (nama, usia, tinggi_badan, menikah) #tidak bisa dimanipulasi. 1 kali deklarsi
dataSet = {1,2,3,4,5} # tidak boleh sama di dalam data set
dataDict = {
    "nama":"Fikri",
    "usia":"20",
    "menikah": False
}

print(nama)
print(type(nama))
print(usia)
print(type(usia))
print(menikah, type(menikah))

print(tinggi_badan, type(tinggi_badan))
print(biodata, type(biodata))
print(biodataTupple, type(biodataTupple))
print(dataSet, type(dataSet))
print(dataDict, type(dataDict))
print(dataDict["menikah"])
"""

data = []

datatupple = ("nama", "usia","asal kampus", "semester")

data.append(input(f"masukkan {datatupple[0]}"))
data.append(input(f"masukkan {datatupple[1]}"))
data.append(input(f"masukkan {datatupple[2]}"))
data.append(input(f"masukkan {datatupple[3]}"))

print(f"{datatupple[0]}: {data[0]}")
print(f"{datatupple[1]}: {data[1]}")
print(f"{datatupple[2]}: {data[2]}")
print(f"{datatupple[3]}: {data[3]}")