# Un dictionar este o structura de date care stocheaza informatii sub forma de perechi cheie-valoare; fiecare informatie se identifica printr-o cheie

persoana = {
    "nume": "Andrei",
    "varsta": 25,
    "oras": "Cluj"
}

persoana_lista = ["Andrei", 25, "Cluj"]
# persoana_lista[0] # nume
# persoana_lista[1] # varsta
# persoana_lista[2] # oras

# print(persoana)
# print(persoana["nume"])
# Folosim dictionare atunci cand vrem sa reprezentam date care au o structura clara

# 1. Crearea unui dictionar
student = {} # un dictionar fara date
# print(student)
# student["nume"] = "Florin"
# print(student)
# student["varsta"] = 26
# print(student)
# student["oras"] = "Cluj"
# print(student)

# Dictionar cu valori initiale - linia 3
persoana = {
    "nume": "Andrei",
    "varsta": 25,
    "oras": "Cluj"
}

# Chei si valori - in dictionar exista 2 componente importante - cheie:valoare
telefon = {
    "brand": "Samsung",
    "model": "Note10",
    "pret": 4200
}

# Tipuri de date pentru chei
# Cel mai des folosim chei de tip "str"

calificative = { # cheie de tip intreg, recomandat sa folosim stringuri
    1: "insuficient",
    2: "suficient",
    3: "bine"
}
# print(calificative[2])

# Tipuri de date pentru valori - string, float, boolean, lista etc

# Accesare valori din dictionar - pentru a accesa o valoare, folosim cheia
persoana = {
    "nume": "Andrei",
    "varsta": 25,
    "oras": "Cluj"
}
# print(persoana["nume"])
# 1. Python cauta cheia "nume" in dictionar si returneaza valoarea asociata

# Daca cheia nu exista
# print(persoana["experienta"]) # KeyError - accesam o cheie care nu exista

# Metoda get() - putem accesa o valoare fara sa primim o eroare - va returna None daca cheia nu exista
# print(persoana.get("nume"))
# print(persoana.get("experienta"))

# la metoda get(), adaugam valoare implicita
# print(persoana.get("experienta", "nu exista cheia experienta"))

# Cum verificam o cheie - operatorul in
# if "nume" in persoana:
#     print(persoana.get("nume"))
# else:
#     print("numele lipseste")

# print("Andrei" in persoana) # False - pentru ca "Andrei" este valoare, nu cheie
# print(persoana.values()) # Returneaza valorile din dictionar
# print(persoana.keys()) # Returneaza cheile din dictionar
# print(persoana.items()) # Returneaza in perechi cheia cu valoarea asociata

# Comparatii
# print("nume" in persoana) # True - cauta cheia
# print("Andrei" in persoana) # False - cauta cheia "Andrei", nu valoarea
# print(persoana.values()) # True - cauta valoarea
# print(persoana.keys()) # True - cauta cheia

# Adaugare perechi noi in dictionar
# persoana["sector"] = 1
# print(persoana)

# Modificare valoare existenta
# persoana["nume"] = "Mihai"
# print(persoana)

# Stergere elemente din dictionar
# del
# del persoana["sector"] # sterge cheia "sector" si valoarea asociata; daca vrem sa stergem o cheie care nu exista, primim KeyError
# print(persoana)

# metoda pop() - sterge cheia si returneaza valoarea stearsa
# persoana["sector"] = 1
# print(persoana)
# cheie_stearsa = persoana.pop("sector")
# print(cheie_stearsa)
# print(persoana)

# metoda clear() - sterge toate elementele din dictionar
# persoana.clear()
# print(persoana)

# Append - nu putem folosi append direct pe dictionar, se poate folosi daca avem de exemplu o lista ca si valoare a unei chei
# persoana = {
#     "nume": "Andrei",
#     "varsta": [25, 26]
# }
#
# persoana["varsta"].append(27)
# print(persoana)


# Parcurgerea unui dictionar - 3 variante
# parcurgem cheile
# parcurgem valorile
# le parcurgem pe amandoua in acelasi timp

# parcurgerea cheilor
persoana = {
    "nume": "Andrei",
    "varsta": 25,
    "oras": "Cluj"
}
# for cheie in persoana: # cand parcurgem direct dictionarul, se parcurg cheile
#     print(cheie)

# parcurgerea valorilor
# for valoare in persoana.values(): # returneaza valorile din dictionar
#     print(valoare)

# parcurgerea cheilor si valorilor
# for cheie, valoare in persoana.items(): # in bucla, python desparte fiecare pereche in doua variabile: cheie, valoare
#     print(f"{cheie} -> {valoare}")

# metode importante pentru dictionare
# 1. keys() - returneaza cheile
# 2. values() - returneaza valorile
# 3. items() - returneaza perechile cheie valoare
# 4. update() - actualizeaza un dictionar cu date din alt dictionar
date_noi = {
    "oras": "Timisoara",
    "inaltime": 1.92
}
# persoana.update(date_noi)
# print(persoana)

# Dictionare cu liste ca valori
elev = {
    "nume": "Florin",
    "note": [8, 9, 10]
}
# Putem accesa lista
# print(elev["note"])

# Putem accesa si o nota individuala din lista
# print(elev["note"][0]) # ia primul element din lista

# adaugarea unei valori intr-o lista din dictionar
# elev["note"].append(7)
# print(elev)

# Lista de dictionare
# Fiecare element din lista este un dictionar
studenti = [
    {
        "nume": "Andrei",
        "nota": 9
    },
    {
        "nume": "Florin",
        "nota": 4
    },
    {
        "nume": "Denisa",
        "nota": 10
    }
]

# parcurgere lista de dictionare
# for student in studenti:
#     print(student["nume"], student["nota"])

# Dictionar de dictionare
produse = {
    "produs1": { # produs1 -> dictionar cu date despre PC
        "nume": "PC",
        "pret": 10000
    },
    "produs2": { # produs2 -> dictionar cu date despre TV
        "nume": "TV",
        "pret": 4000
    }
}

# accesam pretul PC ului
# print(produse["produs1"]["pret"]) # ia valoarea de la cheia "pret" din dictionarul produsului

# exemplu baza de date simpla - dictionar de dictionare
# useri = {
#     "admin": {
#         "parola": "admin",
#         "rol": "administrator"
#     },
#     "user": {
#         "parola": "user123",
#         "rol": "utilizator"
#     }
# }
# username = input("username: ")
# parola = input("parola: ")
#
# if username in useri: # verificam daca userul exista in dictionar
#     user = useri[username] # daca da, luam datele acelui user
#
#     if parola == user["parola"]:
#         print("Autentificare ok")
#         print(f"Rol: {user["rol"]}")
#     else:
#         print("Parola gresita")
# else:
#     print("userul nu exista")


# copierea dictionarelor - varianta NOK
# student1 = {
#     "nume": "Andrei",
#     "nota": 9
# }
#
# student2 = student1
# student2["nota"] = 10
#
# print(student1)
# print(student2)
#
# print(id(student1))
# print(id(student2))

# varianta OK
# copy()
# student1 = {
#     "nume": "Andrei",
#     "nota": 9
# }
#
# student2 = student1.copy()
# student2["nota"] = 10
#
# print(student1)
# print(student2)
#
# print(id(student1))
# print(id(student2))


# student1 = {
#     "nume": "Andrei",
#     "nota": 9
# }
#
# student2 = {}
# student2["nume"] = student1["nume"]
#
# print(student1)
# print(student2)

# Recap
# un dictionare are cheie-valoare
persoana = {
    "nume": "Andrei",
    "varsta": 25,
    "oras": "Cluj"
}

# accesare valoare a unei chei
print(persoana["nume"])

# modificare valoare
persoana["varsta"] = 26
print(persoana)

# adaugare cheie-valoare
persoana["tara"] = "Romania"
print(persoana)

# stergere
del persoana["tara"]
print(persoana)

# accesare sigura
print(persoana.get("tara", "nu exista cheia tara"))

# parcurgere
for cheie, valoare in persoana.items(): # items() ne ajuta sa parcurgem si cheia si valoarea dictionarului
    print(cheie, valoare)
# values() - cand parcurgem doar valori
# keys() - cand parcurgem chei / DE RETINUT: daca nu specificam .keys(), Python parcurge oricum doar cheile
for cheie in persoana:
    print(cheie)


