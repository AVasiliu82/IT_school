# recapitulare

# Variabila - este un loc din memorie in care stocam o valoare
# Exemple:
#nume = "Ana" # stocheaza un text
# varsta = 20 # stocheaza un numar intreg
# inaltime = 1.60 # stocheaza un numar zecimal

# semnul " = " -> pune valoarea din dreapta in variabila din stanga

# print() -> afiseaza informatii pe ecran
# Exemplu:

# print("Salut")
# print(10)

# De ce folosim print?
# 1. Afisam texte
# 2. Afisam valori numerice
# 3. Afisam variabile
# 4. Verificam daca programul face ceea ce ne asteptam

# Exemplu:
# print(nume)

# Putem afisa direct o valoare sau o variabila
# print("Florin")
# print(25)
#
# varsta = 25
# print(varsta)

# print(nume, varsta) # Python pune automat spatiu intre ele atunci cand sunt separate prin virgula

# Putem afisa si text si variabile
# print("Numele meu este:", nume)

# Mai multe moduri de afisare cu print()

# Varianta 1 - cu virgula in print()
# nume = "Maria"
# varsta = 22
#
# print("Numele este", nume)
# print("Varsta", varsta)

# Varianta 2 - cu + intre stringuri
# prenume = "Ion"
# nume_familie = "Popescu"
#
 # print(prenume + " " + nume_familie) # " " -> un string care contine un spatiu, pentru a separa prenumele de numele de familie
# + -> lipeste textele (in cazul nostru, nume si prenume_familie)
# cu +, ambele parti trebuie sa fie stringuri(variabilele prenume si nume_familie in cazul nostru)

# Ok
# oras = "Timisoara"
# print("Locuiesc in " + oras)

# NOK
# varsta = 25
# print("Am " + varsta + " ani") # eroare, pentru ca varsta este un numar intreg, nu un string
# Varianta corectata
#print("Am " + str(varsta) + " ani") # str() -> converteste un numar intr-un string

# Varianta 3 - cu f-string / cu acolade {}

# nume = "Andrei"
# varsta = 21
#
# print(f"Numele meu este {nume} si am {varsta} ani")
# litera f inainte de string spune ca in interior vom pune variabile
# variabilele se scriu intre acolade {}

# Varianta 4 - cu metoda format()
# nume = "Elena"
# varsta = 20
# oras = "Cluj"
# #
# print("Ma numesc {} si am {} ani".format(nume, varsta, oras))

# Tipuri de date in Python
# un tip de date arata ce fel de valoare avem intr-o variabila
# un nume este text
# o varsta este un numar intreg
# o inaltime este un numar zecimal/flotant
# o valoare de tip da/nu poate fi adevarata sau falsa

# python trebuie sa stie ce fel de informatie pastreaza, pentru ca fiecare tip de date se comporta diferit

# 1. str - string - text
# string reprezinta textul
# Exemple
nume = "Ana"
oras = "Cluj"
mesaj = "Salut"

a = "Python"
b = 'curs'
# Observatie: Chiar daca scriem cifre intre ghilimele, ele vor fi considerate tot text - Ex: "123" este un string, nu un numar

# Triple quotes - pentru stringuri care contin mai multe randuri
# Exemplu comentariu pe mai multe randuri
"""
Acesta este un comentariu 
care contine mai multe randuri
"""

# nume = "Alex"
text = f"""Acesta este un text cu 
numele
care contine 
mai multe randuri
si se scrie 
intre triple quotes"""

#print(text)

# Diferenta dintre " " si """ """
# cu ghilimele normale scriem de obicei texte pe o singura linie
# cu ghilimele triple putem scrie texte mai lungi, pe mai multe linii

# \n - inseamna "treci pe linia urmatoare"
#print("\nSalutare\nBine aivenit\nLa curs\n") # textul este scris intr-o singura linie de cod, dar la afisare apare pe mai multe linii
# print("Meinu:\n1. Pizza\n2. paste\n3. Sucuri")

# int - integer - numar intreg - numere fara zecimale

varsta = 25
an = 2026
numar_persoane = 16

# float - numar zecimal
inaltime = 1.75
pret = 19.99
temperatura = 15.5
# In python, zecimalele se scriu cu punct, nu cu virgula
print(15.5) # OK
print(15, 5 + 2) # NOK

# bool - boolean - adevarat sau fals
# acest tip de date are doar doua valori: True (adevarat) sau False (fals)

invata_python = True
este_ziua_mea = False

variabila = None




