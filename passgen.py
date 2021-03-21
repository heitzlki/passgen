import random
chars = ("abcdefghijklmnopqrstuvwxyz1234567890")
try:
    anzahl = int(input("Wie viel Passwörter willst du haben?"))
except:
    anzahl = 1
    print("Variable muss eine Zahl sein... autoassigned: 1")
try:
    länge = int(input("passwort länge ?"))
except:
    länge = 13
    print("Länge muss eine Zahl sein, autoassigned: 13")
for i in range(anzahl):
  passwort ="".join(random.choices(chars,k = länge))
  print(passwort)