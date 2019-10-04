# Dziala dobrze dla "Kurs Pythona jest prosty i przyjemny."
sentence = input("Wpisz dowolne zdanie: ")
print("="*10)
print("Twoje zdanie zawiera ", len(sentence), " znakow")
# Numeracja idzie od zera
print("Drugi wyraz to: ", sentence.split()[1])
print("Siodmy znak to: \"", sentence[6], "\"")
print("Dwunasty znak to: \"", sentence[11], "\"")
print("Czwarty znak od konca to: \"", sentence[-4], "\"")
print("37 znak to: \"", sentence[36], "\"")

