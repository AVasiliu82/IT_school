# Recap metode utile
# d.keys() - toate cheile
# d.values() - toate valorile
# d.items() - perechi cheie-valoare
# d.update(d2) - imbina cu alt dictionar
# d.copy() - copie superficiala
# d.clear() - sterge intreg dictionarul / goleste
# "nume_cheie" in d - verifica existenta cheii

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 2, "c": 4}
# d3 = d1 | d2 # combinare - ia toate perechile cheie-valoare din d1 si d2 si creeaza un dictionar nou

# d3 = d1.copy()
# d3.update(d2)
# print(d3)
# simbolul " | " - reuniune
# simbolul " & " - intersectie - ia elementele comune din colectiile de date dorite

# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5}
#
# print(a & b)
#
# print(d1.keys() & d2.keys())

# Exercitiul 1: Creeaza un dictionar numit user cu informatiile:
# username
# email
# varsta
# oras
# Afisati informatiile pe rand

# user = {
#     "username": "florin",
#     "email": "florin@yahoo.com",
#     "varsta": 26,
#     "oras": "Timisoara"
# }
# print("User: ", user['username'])
# print("Email: ", user['email'])
# print("Varsta: ", user['varsta'])
# print("Oras: ", user['oras'])

# Exercitiul 2: Se da dictionarul:
produs = {
    "nume": "Tastatura",
    "pret": 250,
    "stoc": 10
}
# Modifica pretul la 220
# Adauga "categorie" cu valoarea "Periferice"
# Scade stocul cu 1
# Afiseaza dupa modificari

# produs["pret"] = 220
# produs["categorie"] = "periferice"
# produs["stoc"] -= 1
# print(produs)

# Exercitiul 3 - folosind dictionarul de la ex 2
# Citeste de la tastatura o cheie; daca cheia exista, afiseaza valoarea; daca nu exista, afiseaza "Informatia nu exista"

# 1.
# cheie = input("Introdu cheia: ")
# valoare = produs.get(cheie, "Informatia nu exista")
# print(valoare)

# 2.
# cheie = input("Introdu cheia: ")
# if cheie in produs:
#     print(produs[cheie])
# else:
#     print("Informatia nu exista")

# Exercitiul 4:
produs = {
    "nume": "Tastatura",
    "pret": 250,
    "stoc": 10
}
# Daca pretul este mai mare de 100, se aplica reducere 15%, dupa care afisam pretul final
# Initial printati si pretul inainte de reducere
# print("Pret initial", produs["pret"])

# Exercitiul 5: Se da dictionarul:
produse = {
    "mouse": 80,
    "tastatura": 150,
    "monitor": 900,
    "cablu": 110,
    "casti": 250
}
# Numara cate produse au pretul sub 200 si cate au pretul cel putin 200
# prod_ieftine = 0
# prod_scumpe = 0
#
# for cheie, valoare in produse.items():
#     if valoare < 200:
#         prod_ieftine += 1
#         print(f"Produs ieftin: {cheie} - {valoare}")
#     elif valoare >= 200:
#         prod_scumpe += 1
#         print(f"Produs scump: {cheie} - {valoare}")
# print("Produse ieftine: ", prod_ieftine)
# print("Produse scumpe: ", prod_scumpe)

# Exercitiul 6: Vreau sa creez un dictionar folosind functia input, atat pentru chei cat si pentru valori astfel incat:
# 1. Dictionarul sa aibe numar variabil de perechi
# 2. La final, sa printez dictionarul

dictionar = {}

numar_perechi = int(input("cate perechi adaugi? -> "))

for i in range(numar_perechi):
    cheie = input("Introdu cheie: ")
    valoare = input(f"Introdu valoarea pentru cheia {cheie}: ")

    # Varianta 1: chinezeasca
    # tip_cheie = input("Ce tip de date are cheia? ->")
    # if tip_cheie == "int":
    #     valoare = int(input(f"Introdu valoarea pentru cheia {cheie}: "))
    # else:
    #     valoare = input(f"Introdu valoarea pentru cheia {cheie}: ")

    # Varianta 2:
    # if valoare.isdigit():
    #     valoare = int(valoare)

    # Varianta 3:
    try:
        valoare = int(valoare)
    except ValueError:
        valoare = valoare

    dictionar[cheie] = valoare
    print(type(dictionar[cheie]))
print("Dictionarul final este: ", dictionar)




