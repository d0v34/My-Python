lista = ["Polak","Rosjanin","Niemiec"]

print(lista)

lista.append("Turek")   #dodoanie elementu do listy

print(lista)
lista.sort()            #sortowanie listy
print(lista)
lista.reverse()         #sortowanie malejące
print(lista)


liczby = [4,53,27,67,9,23,64,4,372]
liczby.sort()
print(liczby)
liczby.sort(reverse=True)
print(liczby)
liczby.remove(4)
print(liczby)

print(liczby[6])
print(liczby[2:5])


sklepzoo = [["pies", "kot", "papuga", "mysz"],[2345, 4563, 7678, 567]]

print(sklepzoo)
print(sklepzoo[0])
print(sklepzoo[0][2])
print(sklepzoo[0][0], " - ", sklepzoo[1][0], "PLN")
print(sklepzoo[0][1], " - ", sklepzoo[1][1], "PLN")
print(sklepzoo[0][2], " - ", sklepzoo[1][2], "PLN")
print(sklepzoo[0][3], " - ", sklepzoo[1][3], "PLN")

mieszana = ["Tytus", "Ola", 220, 14.88, True, "Kraków"]
print(mieszana[4])

#mieszana.sort()         #niedozwolone dla różnych typów danych

miasto = ["Kraków", "Lublin", "Wrocław"]
stolica = ["Warszawa", "Londyn", "Wiedeń"]
miasto = miasto + stolica
print(miasto)
miasto = miasto + ["Koszalin", "Tychy"]
print(miasto)
#miasto = miasto + "Ryn"
#print(miasto)

litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("przed zmianą ", litery)
litery[2:7] = [99, 22, 11]
print("po zmianie", litery)

blitery = litery
print("przed zmianą 1", litery)
print("przed zmianą 2", blitery)
clitery = list(litery)


litery[:] = [101, 102, 103]
#assert litery is blitery

print("po zmianie 1", litery)
print("po zmianie 2", blitery)
print("po zmianie 3", clitery)

x = ["czerwony", "zielony", "niebiski", "czarny", "biały", "granatowy"]
odds = x[::2]       # skok o 2 elementy
evens = x[1::2]
cotrzeci = x[::3]   # skok o 3 elementy
print(x)
print(odds)
print(evens)
print(cotrzeci)

