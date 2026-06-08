# Exercitiul 1: Se citeste de la tastatura un sir de caractere.
# Sa se returneze un dictionar cu numarul de aparitii al fiecarei litere(frecventa, ignoram spatiile, de ex "Ana are mere")

# sir = input("Introdu text: ")
#
# sir = sir.lower()
# frecventa = {}
#
# for caracter in sir:
#     if caracter == " ":
#         continue
#     if caracter in frecventa:
#         #Cazul 1. Daca litera exista deja, marim counterul cu 1
#         frecventa[caracter] += 1
#     else:
#         # Cazul 2. Daca litera nu exista inca in dictionar, o adaugam cu valoarea 1
#         frecventa[caracter] = 1
# print(frecventa)

# sir = input("Introdu text: ")
#
# sir = sir.lower()
# frecventa = {}
#
# for caracter in sir:
#     if caracter == " ":
#         continue
#     frecventa[caracter] = frecventa.get(caracter, 0) + 1
#
# print(frecventa)
# dictionar = {}
# sir = input("Introduceti sirul de caractere: ")
# #valoare = 0
#
# for caracter in sir:
#     if caracter != ' ':
#         #cheie = caracter
#         if caracter in dictionar:
#             dictionar[caracter] += 1
#         else:
#             dictionar[caracter] = 1
# print(dictionar)



# Exercitiul 2: Inversare dictionar. Se da urmatorul dictionar, inverseaza cheile cu valorile. Daca mai multe chei au aceeasi valoare, grupeaza-le intr-o lista
d = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2,
}

# invers = {}
#
# for cheie, valoare in d.items():
#     if valoare in invers:
#         invers[valoare].append(cheie)
#     else:
#         invers[valoare] = [cheie]
# print(invers)


# Exercitiul 3: Imbina doua dictionare. Ai doua depozite cu fructe reprezentate ca dictionare. Scrie o functie care imbina cele doua depozite intr-unul singur.
# Daca un produs apare in ambele, cantitatile se aduna

# De ex:
d1 = {"mere": 20, "pere": 5}
d2 = {"mere": 3, "banane": 16}

def depozite(dep1, dep2):
    result = dep1.copy()
    for cheie, valoare in dep2.items():
        if cheie in result:
            result[cheie] = result[cheie] + valoare
        else:
            result[cheie] = valoare
    return result
depozit = depozite(d1, d2)
print(depozit)