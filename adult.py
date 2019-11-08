print("Ile masz lat?")
age = int(input())
##tofull = 18 - age
if age >= 18:
    print("Jestes pelnoletni")
elif age > 100:
    print ("To naprawde twoj wiek?")
else:
    print("Zostalo ci", 18-age ,"lat do pelnoletnosci")

