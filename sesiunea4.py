# *args - ia toate valorile date si le pune intr-un tuplu

x = "25"
y = int(x) # daca pui y = x da eroare

print (y + 5)

print("10" + "5")
print (10 + 5)

x = "19.99"
#print(type(x))
decimal = float(x)
print(type(decimal))

# operatori_matematici
#simboluri folosite pentru calcule matematice

# + adunare
# - scadere
# * inmultire
# / impartire
# ** ridicare la putere
# // impartirea intreaga
# % restul impartirii

# Adunare

a = 10
b = 5
suma = a+b
print(suma)

#Scadere

diferenta = a-b
print(diferenta)

#Inmultire
produs = a*b
print(produs)

# Impartire
cat = a/b
print(int(cat)) # int ca sa avm intrg - fara zecimale

# :.2f - se foloseste ca sa afisam un numar zecimal cu exact 2 cifre dupa virgula
# f vine de la float
# .2 inseamna 2 zecimale

rezultat = 10/3
print(rezultat)
print(f"{rezultat:.4f}")

#Important - :.2f nu schimba valoare, doar modul de afisare

# Impartirea intreaga
print(10 //3)
# pentru ca 10 impartit la 3 este 3.33333... iar // pastreaza doar partea intreaga, adica 3

# restul impartirii
print(10 % 3)
print(8 % 2)

# daca restul este zero stim sigur ca numarul este divizibil cu 2
# util pentru a verifica daca un numar este par sau impar

# puterea
print(2 ** 3)
print(5 ** 2)

# Ordinea operatiilor
#in Python se respecta ordinea matematica a operatiilor
print(2 + 3 * 4) # inmultirea se face inaintea adunarii
print ((2+3) * 4)

# in matematica = inseamna egalitate
# in programare = inseamna atribuire

x = 10 # x peimwste valoarea 10 - pune valoarea 10 in variabila x

#input() - cum citim date de la utilizator
#input este o functie care permite utilizatorului sa scrie ceva de la tastatura

#nume = input("Cum te numesti?")
#print(nume)

#1. programul afiseaza mesajul cum te numesti
#2. utilizatorul scrie ceva
#3. valoarea este salvata in variabila nume

# input() - returneaza intotdeauna text
#varsta = input ("Cati ani ai?")
#print(varsta)
#print(type(varsta)) # o sa fie str

varsta = int(input("Cati ani ai?\n"))
print(varsta)
print(type(varsta))

inaltime = float(input("Ce inaltime ai?\n"))
print(inaltime)
print(type(inaltime))

numar1 = input("Primul numar: ")
numar2 = input("Al doilea numar: ")

print(numar1 + numar2)

numar3 = int(input("Primul numar: "))
numar4 = int(input("Al doilea numar: "))

print(numar3 + numar4)

# exemple de operatii aritmetice

a = 10
b = 3

print("Adunare:", a+b)
print("Scadere:", a-b)
#de completat de la florin

#greseli frrecvente
#nume = Ana - corect e nume =" Ana" - variabilele de tip text/string trebuie sa fie intre ghilimele
#inaltime = 1,75 - corect 1.75 - in Python folosim punctul pentru zecimale

# cand unesti text cu un numar fara conversie
varsta = 20
print ("Am " + str(varsta) + " ani") # trebuie sa convertim variabila varsta la string pentru a putea lipi/concatena textul

#input() - returneaza intotdeauna text/string - ai nevoie sa faci conversie la tipul de date dorit (int. float etc)

# se confunda / cu //
# / - rezultatul decimar
# // - doar partea intreaga

#Exercitii:

#1. Citeste de la tastatura numele utilizatorului si afiseaza un mesaj: Bun venit la curs, X

nume = input("nume: ")
print("Bun venit la c22urs, " + nume)

#2. Citeste de la tastatura 2 numere intregi si afiseaza suma lor

numar_1 = int(input("numar_1: "))
numar_2 = int(input("numar_2: "))

#suma = numar_1 + numar_2

#print(f"Suma numerelor este {suma}")

#3. Citeste de la tastatura 2 numere intregi si afiseaza suma, scaderea, inmultirea si impartirea

suma = numar_1 + numar_2
print(f"Suma numerelor este {suma}")

diferenta = numar_1 - numar_2
print(f"Diferenta numerelor este {diferenta}")

produs = numar_1 * numar_2
print(f"Produsul numerelor este {produs}")

cat = numar_1 / numar_2
print(f"Catul numerelor este {cat}")

#4. Citeste varsta si afiseaza peste 5 ani vei avea X ani

varsta = int(input("Varsta este: "))
varsta_viitoare = varsta + 5
print(f"Peste 5 ani voi avea {varsta_viitoare}")

#5. Citeste un pret si o cantitate si calculeaza costul final

pret = float(input("Pretul este: "))
cantitate = int(input("Cantitatea este: "))

cost_final = pret * cantitate

print(cost_final)
print(f"Costul total platit va fi {cost_final:.1f}")