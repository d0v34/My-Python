# słownik - dictionary = para klucz, wartość

auto = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1972
}

print(auto)

print(auto["model"])
m = auto["model"]

print(m)

mg = auto.get("model")
print(mg)

auto["rocznik"] = 2018
print(auto)

print(auto.items())
print(auto.keys())
print(auto.values())

for x in auto:
    print(x)

for y in auto:
    print(auto[y])


for x,y in auto.items():
    print(x, ": ", y)



auta = {
    "auto1":{
        "marka": "Ford",
        "model": "Mustang",
        "rocznik": 1972
    },
"auto2":{
        "marka": "Fiat",
        "model": "Punto",
        "rocznik": 2001
    },
"auto3":{
        "marka": "Toyota",
        "model": "Yaris",
        "rocznik": 2009
    },
"auto4":{
        "marka": "Subaru",
        "model": "Forester",
        "rocznik": 2011
    }
}

print(auta)

for i in auta.values():
    print(i)


