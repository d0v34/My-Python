drzewa = {"dąb", "buk", "sosna", "jesion", "baobab", "jabłoń", "grusza", "świerk"}

print(drzewa)
print(drzewa)
print(drzewa)

for d in drzewa:
    print(d)

print("jesion" in drzewa)
print("osika" in drzewa)


drzewa.add("osika")
drzewa.add("osika")             # nie da sie dwa razy dodać tego samego, brak błędu
print(drzewa)

drzewa.update(["topola", "wierzba", "cedr"])            # można dodać liste albo krotkę
print(drzewa)

drzewa.remove("osika")
print(drzewa)

#drzewa.remove("jojoba")            # błąd bo brak elementu w zbiorze
drzewa.discard("jojoba")            # brak błędu nawet jak nie ma elementu w zbiorze
print(drzewa)

drzewa_m = drzewa.pop()             # zdejmuje 1 ze zbioru element
print(drzewa_m)
print(drzewa)

dlista = list(drzewa)
print(dlista)

zbdrzewa = set(dlista)
print(zbdrzewa)
