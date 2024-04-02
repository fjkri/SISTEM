

f = open("data.json", "a")
data = {
    "nama":"Fikri",
    "usia":19
}
f.write("{\n")
f.write(f"{data}")
f.write("}")
f.close()