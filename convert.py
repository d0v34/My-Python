# print("Podaj watosc w cm")
# i = input()
# To mozna w jednej lini
i = int(input("poedaj dlugosc w cm: "))
i = i / 100
print("Wartosc w metrach wynosi {} m".format(i))
# To bedzie to samo
print("Wartosc w metrach wynosi %.2f m" % (i))
# tylko python3!!!
