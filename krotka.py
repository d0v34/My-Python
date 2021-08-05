#krotka = tuple
animal = ("pies", "kot", "papuga", "królik")
print(animal)
print(animal[2])

for i in animal:
    print(i)


if "kot" in animal:
    print("OK")

if "budynek" in animal:
    print("OK")
else:
    print("Not in table")


animal2 = ("pająk", "żaba")

animal = animal + animal2
print(animal)

mojakrotka = tuple(["aaa", "sss", "ddd"])       # krotka z listy
print(mojakrotka)

mojalista = list(mojakrotka)                    # lista z krotki
mojalista.append("fff")
mojalista.sort()
print(mojalista)
drugakrotka = tuple(mojalista)                  # ponownie krotka z listy
print(drugakrotka)

#lista w nawiasach []
#krotka w nawiasach ()

auto = ('audi', 'q7', 3.8, 2020)
(marka, model, poj, rok) = auto                 # belka = nazwa rekordu = zmienne przypisane do krotki
print(marka)
print(rok)
