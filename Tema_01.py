# *******************
# Exercitiul 1
# Creeaza 3 variabile:
# nume
# varsta
# oras
# Atribuie valori si afiseaza-le fiecare pe rand cu print().

# Rezolvare exercitiul 1:
nume = "Andi"
varsta = 43
oras = "Bucuresti"

print(nume)
print(varsta)
print(oras)

# *******************
# Exercitiul 2
# Creeaza variabilele:

# prenume = "Ana"
# an_nastere = 2002
# inaltime = 1.68

# Afiseaza valorile intr-un mod clar, ca in exemplu:
# Prenume: Ana
# An nastere: 2002
# Inaltime: 1.68

# Rezolvare exercitiul 2:
# Creează variabilele
prenume = "Ana"
an_nastere = 2002
inaltime = 1.68

# Afișează valorile clar
print("Prenume:", prenume)
print("An nastere:", an_nastere)
print("Inaltime:", inaltime)

# *******************
# Exercitiul 3
# Creeaza doua variabile de tip string:
# prenume
# nume_familie
# Afiseaza numele complet folosind concatenare cu +.
# Exemplu rezultat:
# Andrei Popescu

# Rezolvare exercitiul 3:
# Creează variabilele
prenume = "Andrei"
nume_familie = "Popescu"

# Afișează numele complet folosind concatenare
nume_complet = prenume + " " + nume_familie
print(nume_complet)

# *******************
# Exercitiul 4
# Creeaza variabilele:
# oras = "Timisoara"
# tara = "Romania"
# Afiseaza propozitia:
# Locuiesc in Timisoara, Romania
# Rezolva folosind print() cu virgula intre elemente.

# Rezolvare exercitiul 4:

# Creează variabilele
oras = "Timisoara"
tara = "Romania"

# Afișează propoziția folosind virgule
print("Locuiesc in", oras + ",", tara)
# *******************


# Exercitiul 5
# Creeaza variabilele:
# nume = "Maria"
# varsta = 22
# Afiseaza propozitia:
# Maria are 22 ani
# Rezolva prin concatenare cu +, deci trebuie sa folosesti si str().

# Rezolvare exercitiul 5:

nume = "Maria"
varsta = 22

propozitie = nume + " are " + str(varsta) + " ani"
print(propozitie)

# *******************
# Exercitiul 6
# Refa exercitiul 5, dar de data aceasta folosind f-string.

# Rezolvare exercitiul 6:
# Creează variabilele
nume = "Maria"
varsta = 22

# Afișează propoziția folosind f-string
print(f"{nume} are {varsta} ani")

# *******************
# Exercitiul 7
# Refa exercitiul 5, dar de data aceasta folosind .format().

# Rezolvare exercitiul 7:
# Creează variabilele
nume = "Maria"
varsta = 22

# Afișează propoziția folosind .format()
print("{} are {} ani".format(nume, varsta))

# *******************
# Exercitiul 8
# Creeaza 4 variabile:
# produs = "lapte"
# pret = 8.5
# cantitate = 2
# magazin = "Lidl"
# Afiseaza o propozitie la alegere care sa contina toate aceste informatii.
# Exemplu:
# Am cumparat 2 bucati de lapte din Lidl la pretul de 8.5 lei

# Rezolvare exercitiul 8:
# Creează variabilele
produs = "lapte"
pret = 8.5
cantitate = 2
magazin = "Lidl"

# Afișează propoziția
print(f"Am cumparat {cantitate} bucati de {produs} din {magazin} la pretul de {pret} lei")

# *******************
# Exercitiul 9
# Creeaza un mini-cartonas de prezentare cu:
# nume
# varsta
# oras
# ocupatie
# Afiseaza totul pe mai multe linii folosind \n.

# Rezolvare exercitiul 9:

# Creează variabilele
nume = "Maria"
varsta = 22
oras = "Cluj-Napoca"
ocupatie = "Student"

# Afișează mini-cartonașul pe mai multe linii
print("Nume: " + nume + "\nVarsta: " + str(varsta) + "\nOras: " + oras + "\nOcupatie: " + ocupatie)


# *******************
# Exercitiul 10
# Scrie un text pe mai multe randuri folosind triple quotes """ """.

# Rezolvare exercitiul 10:
text = """Acesta este un text
scris pe mai multe rânduri,
foarte multe ghilimele."""

print(text)


# *******************
# Exercitiul 11
# Creeaza variabilele:
# zi = "luni"
# temperatura = 23.5
# Afiseaza propozitia:
# Astazi este luni si sunt 23.5 grade afara
# Fa exercitiul in 2 variante:
# cu f-string
# cu .format()

# Rezolvare exercitiul 11:
zi = "luni"
temperatura = 23.5

# Varianta 1: cu f-string
print(f"Astazi este {zi} si sunt {temperatura} grade afara")

# Varianta 2: cu .format()
print("Astazi este {} si sunt {} grade afara".format(zi, temperatura))

# *******************
# Exercitiul 12
# Creeaza variabile pentru 3 colegi:
# coleg1
# coleg2
# coleg3
# Afiseaza propozitia:
# In grupa mea sunt: X, Y si Z

# Rezolvare exercitiul 12:
coleg1 = "Andrei"
coleg2 = "Andreea"
coleg3 = "Ionut"

# Folosind f-string pentru simplitate
print(f"In grupa mea sunt: {coleg1}, {coleg2} si {coleg3}")

# *******************
# Exercitiul 13
# Creeaza variabilele:
# marca = "Audi"
# model = "A4"
# an = 2007
# Afiseaza:
# Masina mea este un Audi A4 din anul 2007
# Foloseste concatenare cu +.

# Rezolvare exercitiul 13:
marca = "Audi"
model = "A4"
an = 2007

# Folosim str(an) pentru a putea uni numărul cu restul textului
print("Masina mea este un " + marca + " " + model + " din anul " + str(an))

# *******************
# Exercitiul 14
# Creeaza 3 variabile booleene:
# are_tema
# este_prezent
# a_invatat_python
# Atribuie valori True sau False si afiseaza-le.
# Exemplu:
# Are tema: True

# Rezolvare exercitiul 14:
are_tema = True
este_prezent = False
a_invatat_python = True

print(f"Are tema: {are_tema}")
print ("Are tema:", are_tema)
print(f"Este prezent: {este_prezent}")
print(f"A invatat Python: {a_invatat_python}")

# *******************
# Exercitiul 15
# Creeaza urmatoarele variabile:
# nume = "Florin"
# job = None
# salariu = 5000
# Afiseaza-le pe toate si observa cum se afiseaza valoarea None.

# Rezolvare exercitiul 15:
nume = "Florin"
job = None
salariu = 5000

print(f"Nume: {nume}")
print(f"Job: {job}")
print(f"Salariu: {salariu}")

# *******************
# Exercitiul 16
# Creeaza variabilele:
# materie1 = "Python"
# materie2 = "SQL"
# materie3 = "Testing"
# Afiseaza un “orar” pe mai multe linii folosind \n.

# Rezolvare exercitiul 16:
materie1 = "Python"
materie2 = "SQL"
materie3 = "Testing"

# \n mută cursorul pe rândul următor
print(f"Orarul meu este:\n1. {materie1}\n2. {materie2}\n3. {materie3}")

# *******************
# Exercitiul 17
# Creeaza variabilele:
# prenume = "Ioana"
# varsta = 19
# inaltime = 1.72
# este_elev = True
# Afiseaza toate informatiile intr-o singura propozitie, folosind f-string.

# Rezolvare exercitiul 17:
prenume = "Ioana"
varsta = 19
inaltime = 1.72
este_elev = True

print(f"Prenumele este {prenume}, are vârsta de {varsta} ani, o înălțime de {inaltime}m și este elev: {este_elev}.")

# *******************
# Exercitiul 18
# Creeaza doua variabile string:
# cuvant1 = "Hello"
# cuvant2 = "Python"
# Afiseaza:
# cele doua cuvinte separate prin spatiu
# cele doua cuvinte pe linii diferite

# Rezolvare exercitiul 18:
cuvant1 = "Hello"
cuvant2 = "Python"

# Afișare cu spațiu între ele
print(f"{cuvant1} {cuvant2}")

# Afișare pe linii diferite folosind \n
print(f"{cuvant1}\n{cuvant2}")

# *******************
# Exercitiul 19
# Creeaza variabilele:
# nume_film
# an_aparitie
# nota
# Afiseaza o propozitie de forma:
# Filmul X a aparut in anul Y si are nota Z
# Rezolva in 3 moduri:
# cu virgula in print()
# cu f-string
# cu .format()

# Rezolvare exercitiul 19:
nume_film = "Inception"
an_aparitie = 2010
nota = 8.8

# Varianta 1: cu virgulă în print() (adaugă automat spații)
print("Filmul", nume_film, "a aparut in anul", an_aparitie, "si are nota", nota)
print ("Filmul {} a aparut in {} si are nota {}".format(nume_film,an_aparitie,nota))

# Varianta 2: cu f-string (cea mai lizibilă metodă)
print(f"Filmul {nume_film} a aparut in anul {an_aparitie} si are nota {nota}")

# Varianta 3: cu .format()
print("Filmul {} a aparut in anul {} si are nota {}".format(nume_film, an_aparitie,))

# *******************
# Exercitiul 20
# Fa o descriere completa despre tine sau despre o persoana inventata, folosind:
# minimum 6 variabile
# cel putin un int
# cel putin un float
# cel putin un bool
# text afisat pe mai multe linii
# cel putin o propozitie cu f-string

# Rezolvare exercitiul 20:

