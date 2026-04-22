# *args - ia toate valorile date fara nume si le pune intr-un tuplu

# x = "25"
# y = int(x)
# # print(x + 5)
# print("10" + "5")
# print(10 + 5)
#
# x = "19.99"
# print(type(x))
# decimal = float(x)
# print(type(decimal))

# operatori aritmetici
# simboluri folosite pentru calcule matemtice

# + -> adunare
# - -> scadere
# * -> inmultire
# / -> impartire
# ** -> ridicare la putere
# // -> impartirea intreaga
# % -> restul impartirii

# Adunare
a = 10
b = 5
suma = a + b
print(suma)

# Scadere
diferenta = a - b
print(diferenta)

# Inmultire
produs = a * b
print(produs)

# Impartire
cat = a / b
print(int(cat))

# :.2f -> se foloseste ca sa afisam un numar zecimal cu exact 2 cifre dupa virgula
# f vine de la float
# .2 inseamna 2 zecimale

rezultat = 10 / 3
print(rezultat)
print(f"{rezultat:.4f}")
# Important: :.2f nu schimba valoarea, doar modul de afisare

# impartirea intreaga
print(10 // 3)
# pentru ca 10 impartit la 3 este 3.3333.. iar // pastreaza doar partea intreaga, adica 3

# restul impartirii
print(10 % 3)
print(8 % 2)
# daca restul este 0, numarul este divizibil cu 2
# util pentru a verifica daca un numar este par sau impar

# puterea
print(2 ** 3)
print(5 ** 2)

# Ordinea operatiilor
# in python se respecta ordinea matematica a operatiilor
print(2 + 3 * 4)  # inmultirea se face inaintea adunarii
print((2 + 3) * 4)

# in matematica = inseamna egalitate
# in programare = inseamna atribuire
x = 10  # x primeste valoarea 10 -> pune valoarea 10 in variabila x

# input() - cum citim date de la utilizator
# input este o functie care permite utilizatorului sa scrie ceva de la tastatura

# nume = input("Cum te numesti? ")
# print(nume)
#
# # 1. programul afiseaza mesajul cum te numesti?
# # 2. utilizatorul scrie ceva
# # 3. valoarea introdusa este salvata in variabila nume
#
# # input() -> returneaza intotdeauna text
# varsta = input("Cati ani ai?\n ")
# print(varsta)
# print(type(varsta))

# varsta = int(input("Cati ani ai?\n"))
# print(varsta)
# print(type(varsta))
#
# inaltime = float(input("Ce inaltime ai?\n"))
# #print(inaltime)
# print(type(inaltime))

# numar1 = input("Primul numar: ")
# numar2 = input("Al doilea numar: ")
#
# print(numar1 + numar2)
#
# numar1 = int(input("Primul numar: "))
# numar2 = int(input("Al doilea numar: "))
#
# print(numar1 + numar2)

# exemple operatii aritmetice
a = 10
b = 3
print("Adunare:", a + b)
print("Scadere:", a - b)
print("Inmultire:", a * b)
print("Impartire:", a / b)
print("Impartire intreaga:", a // b)
print("Restul impartirii:", a % b)
print("Puterea:", a ** b)

# greseli frecvente
# nume = Ana -> corect: "Ana" ; variabilele de tip text/string trebuie sa fie intre ghilimele
# inaltime = 1,75 -> corect: 1.75 ; in python folosim punctul pentru zecimale

# cand unesti text cu un numar fara conversie
# varsta = 20
# print("Am " + str(varsta) + " ani") # trebuie sa convertim variabila varsta la string pentru a putea lipi/concatena textul

# input() returneaza intotdeauna text/string -> ai nevoie sa faci conversie la tipul de date dorit (int, float etc)

# se confunda / cu //
# / -> rezultatul decimal
# // -> doar partea intreaga

# Exercitii:

# 1. Citeste de la tastatura numele utilizatorului si afiseaza un mesaj : "Bun venit la curs, X"





