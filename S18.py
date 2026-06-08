import json

# student = {
#     "nume": ...,
#     "varsta": ...,
#     "oras": ...,
#     "python": True
# }

# JSON -> JavaScript Object Notation -> format de stocare si transfer date
# Exemple de utilizare:
# 1. config files
# 2. web apps
# 3. APIs
# 4. baze de date
# 5. automatizare

# JSON pastreaza datele intr-o structura clara
# {
#     "nume": "Florin",
#     "varsta": 27,
#     "oras": "Timisoara",
#     "python": true
# }
# Diferente importante intre dictionar si JSON:
# 1. True <-> true
# 2. None <-> null
# 3. dictionar <-> obiect
# 4. lista <-> array
# 5. string cu ghilimele simple sau duble <-> string doar cu ghilimele duble

# Functii
# 1. json.loads() -> transforma un string JSON in obiect Python
# 2. json.dumps() -> transforma un obiect Python in string JSON
# 3. json.load() -> citeste JSON din fisier si il transforma in obiect Python
# json.dump() -> scrie un obiect Python intr-un fisier JSON

# cu s la final: lucreaza cu string
# fara s la final: lucreaza cu fisier

# # 1. json.loads()
# text_json = '{"nume": "Florin", "varsta": 27, "oras": "Timisoara"}'
# persoana = json.loads(text_json)
# print(persoana)
# print(type(persoana))
# # 2. Accesare date dupa ce folosim json.loads()
# print(persoana["nume"])
# print(persoana["varsta"])

# 2. json.dumps()
# persoana = {
#             "nume": "Florin",
#             "varsta": 27,
#             "oras": "ĂÂÎȘȚăâîșț"
# }
#
# text_json = json.dumps(persoana, indent = 4, ensure_ascii = False) # indentare 4 spatii si ascii = False nu transforma caracterele speciale in Unicode
# print(text_json)
# print(type(text_json))

# 3. json.dump()
# persoana = {
#             "nume": "Florin",
#             "varsta": 27,
#             "oras": "Timisoara"
# }
#
# with open("persoana.json", "w", encoding="utf-8") as fisier:
#     json.dump(persoana, fisier, indent = 4)

# 4. json.load()
# with open("persoana.json", "r") as fisier:
#     persoana = json.load(fisier)
# print(persoana)
# print(type(persoana))

# Diferenta intre load() si loads()
# json.loads() -> lucreaza cu string
# json.load() -> lucreaza cu fisiere

# Diferenta intre dump() si dumps()
# json.dump() -> scrie un obiect Python intr-un fisier JSON
# json.dumps() -> transforma un obiect Python in string JSON

# Exemplu:
# lista de dictionare
persoane = [
    {
        "nume": "Florin",
        "varsta": 27,
        "oras": "Timisoara"
    },
{
        "nume": "Andrei",
        "varsta": 30,
        "oras": "Cluj"
    },
{
        "nume": "Ana",
        "varsta": 20
    }
]

# 1. Scriem lista persoane in JSON
# with open("lista_persoane.json", "w") as fisier:
#     json.dump(persoane, fisier, indent = 4)
# 2. Citim o lista de dictionare din JSON
# with open("lista_persoane.json", "r") as fisier:
#     text = json.load(fisier)
# print(text)
# print(type(text))

# 3. Putem parcurga lista respectiva
# for persoana in persoane:
#     print(persoana["nume"], persoana["oras"])

# Adaugare element nou in fisierul JSON
# with open("lista_persoane.json", "r") as fisier:
#     persoane = json.load(fisier)
#
# persoana_nou = {
#     "nume": "Ana",
#     "varsta": 20,
#     "oras": "Craiova"
# }
# # NOK -> va adauga persoana dupa "]" ceea ce este invalid
# with open("lista_persoane.json", "a") as fisier:
#     json.dump(persoana_nou, fisier, indent=4)

# persoane.append(persoana_nou)
#
# with open("lista_persoane.json", "w") as fisier:
#     json.dump(persoane, fisier, indent = 4)

# Modificam un element din JSON
# with open("lista_persoane.json", "r") as fisier:
#     persoane = json.load(fisier)
#
# for persoana in persoane:
#     if persoana["nume"] == "Ana":
#         persoana["oras"] = "Oradea"
#
# with open("lista_persoane.json", "w") as fisier:
#     json.dump(persoane, fisier, indent = 4)

# Stergem un element din JSON
# with open("lista_persoane.json", "r") as fisier:
#     persoane = json.load(fisier)
#
# # persoane_actualizat = []
# for persoana in persoane:
#     if persoana["nume"] == "Mihai":
#         persoane.remove(persoana)
#
# with open("lista_persoane.json", "w") as fisier:
#     json.dump(persoane, fisier, indent = 4)

# Verificam existenta unei chei
# for persoana in persoane:
#     if "oras" in persoana:
#         print(persoana["nume"], persoana["oras"])
#     else:
#         print(persoana["nume"], "nu are cheia oras")

# Aplicatie produse online
# 1. Cauta un produs de la tastatura
# 2. Adauga un produs nou de la tastatura

# 1. cauta produs de la tastatura
with open("produse.json", "r") as fisier:
    produse = json.load(fisier)

# 4. Stergere ID si reasezare automata a ID urilor ramase
id_sters = int(input("Sterge ID: "))

produse_nou = []

for produs in produse:
    if produs["id"] != id_sters:
        produse_nou.append(produs)
        break

id_nou = 1

for produs in produse_nou:
    produs["id"] = id_nou
    id_nou += 1

with open("produse.json", "w") as fisier:
    json.dump(produse_nou, fisier, indent = 4)

# Varianta cu pop()
# for index in range(len(produse)):
#     if produse[index]["id"] == id_sters:
#         produse.pop(index)
#         break
#
# id_nou = 1
#
# for produs in produse:
#     produs["id"] = id_nou
#     id_nou += 1
#
# with open("produse.json", "w") as fisier:
#     json.dump(produse, fisier, indent = 4)


# nume_produs = input("Nume produs: ")
#
# produs_gasit = False
#
# for produs in produse:
#     if produs["nume"].lower() == nume_produs.lower():
#         print(f"S-a gasit produsul {nume_produs} cu ID {produs["id"]}")
#         produs_gasit = True
#         break
#
# if not produs_gasit:
#     print("Produsul nu exista")

# 3. Auto incrementare ID
# id_max = 0
#
# for produs in produse:
#     if produs["id"] > id_max:
#         id_max = produs["id"]
#
# id_nou = id_max + 1


# 2. Adaugare produs nou de la tastatura
# id_nou = int(input("id produs nou: "))
# nume_nou = input("nume produs nou: ")
# pret_nou = int(input("pret produs nou: "))
# stoc_nou = int(input("stoc produs nou: "))
#
# nume_nou = nume_nou.capitalize()
#
# produs_nou = {
#     "id": id_nou,
#     "nume": nume_nou,
#     "pret": pret_nou,
#     "stoc": stoc_nou
# }
#
# produse.append(produs_nou)
#
# with open("produse.json", "w") as fisier:
#     json.dump(produse, fisier, indent = 4)

