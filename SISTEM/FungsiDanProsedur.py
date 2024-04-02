"""# Prosedure
def cetak(nama):
    print("Hello",nama)

# Fungsi
def getNama():
    return "fikri"

cetak("fikri")
getNama()
"""

"""
def getSesuatu(ar):
    data = {
        "nama":"Fikri",
        "usia":20
    }
    return data[ar]

nama = getSesuatu("nama")
usia = getSesuatu("usia")

print(nama)
print(usia)

print(getSesuatu("nama"))
print(getSesuatu("usia"))
"""

"""
def login(username, password):
    if username == "Fikri" and password == "Fikri123":
        return True
    else:
        return False
    
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

if login(username, password):
    print("Berhasil Login")
else:
    print("Gagal Login")
"""

#fungsi lambda
"""
kali = lambda x,y: x*y

print(kali(5,4))

sapa = lambda nama: print(f"Hello {nama}")
sapa("Fikri")
"""

# Parameter
"""
def kali(x,y=2):
    print(x*y)

kali(1)
"""

def tes(*args):
    print(type(args))
    print(args)
    for isi in args:
        print(isi)

print(tes("Fikri","Fahri","Salsa"))


