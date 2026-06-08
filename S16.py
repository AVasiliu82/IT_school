# Un set este o colectie de valori
# 1. nu permite duplicate
# 2. Nu are ordine garantata
# 3. Este modificabil

numere = {1, 2, 3, 4}
# print(type(numere))
# print(numere)

# Exemplu
persoane = ["ana", "mihai", "ana", "george", "mihai"]
persoane_unic = set(persoane)
# print(persoane_unic)

# Creare set
# 1. Cu acolade
fructe = {"mere", "pere", "capsuni"}

# 2. cu functia set()
numere = set([1, 2, 3, 3, 4])
# print(numere)

# 3. Set gol
set_gol = {} # gresit, va crea un dictionar
# print(type(set_gol))

set_gol = set() # corect
# print(type(set_gol))

# Seturile nu permit duplicate
numere = {1, 2, 2, 3, 3, 3, 4} # Seturile sunt construite pentru a retine valori unice
# print(numere)

# Seturile nu au ordinea garantata
culori = {"rosu", "verde", "albastru"} # Setul nu este construit pentru ordine. Pentru seturi avem: unicitate, verificare rapida, operatii intre grupuri de valori
# print(culori)

# Seturile nu se acceseaza cu index
culori = {"rosu", "verde", "albastru"}
# print(culori[0]) # Nu merge, setul nu are pozitii fixe

# Cum parcurgem un set
culori = {"rosu", "verde", "albastru"}
# for culoare in culori:
#     print(culoare)

# Daca ai nevoie sa parcurgi si sa afisezi ordonat, poti folosi sorted()
# for culoare in sorted(culori): # Sorted -> transforma valorile intr-o lista sortata, fara sa modifice setul original
#     print(culoare)

# Verificare existenta valori folosind "in"
culori = {"rosu", "verde", "albastru"}
# if "rosu" in culori: # vrem sa verificam daca o valoare exista in set
#     print("Avem rosu in set")
# else:
#     print("Nu exista rosu in set")

# Adaugarea unui element folosind add()
fructe = {"mere", "pere"}
# fructe.add("portocale")
# print(fructe)

# daca adaug un element care exista deja
# fructe.add("portocale") # nu va afisa al doilea element "portocale" pentru ca nu permite duplicate
# print(fructe)

# Adaugarea mai multor elemente -> update()
fructe = {"mere", "pere"}
# fructe.update(["banane", "portocale", "mere"])
# print(fructe)

a = {1, 2}
b = {3, 4}
# a.update(b)
# print(a)
# print(b)

# pentru string
litere = set()
# litere.update("abc") # python va parcurge stringul caracter cu caracter
# litere.add("abc") # daca vrei sa adaugi "abc" ca un singur element, folosim add()
# print(litere)

# Dfierenta dintre update si add
# add() -> adauga valoarea intreaga, fara sa o sparga in caractere
# update() -> parcurge colectia si adauga fiecare element

# Stergerea unui element -> remove()
nume = {"Florin", "Andrei", "Mihai"}
# nume.remove("Andrei")
# print(nume)
# Daca incercam sa stergem o valoare care nu exista, va afisa KeyError

# Stergerea unui element fara eroare: discard()
nume = {"Florin", "Andrei", "Mihai"}
# nume.discard("Ionut")
# print(nume)

# Stergere element la intamplare: pop()
nume = {"Florin", "Andrei", "Mihai"}
# valoare_stearsa = nume.pop() # sterge si returneaza un element din set; nu poti controla exact care element
# print(valoare_stearsa)
# print(nume)

# Golire set: clear()
nume = {"Florin", "Andrei", "Mihai"}
# nume.clear() # sterge toate elementele din set
# print(nume)

# Lungimea unui set: len()
numere = {1, 2, 2, 3, 3, 3, 4}
# print(len(nume))

# ce tipuri de valori pot exista intr-un set
# 1. int
# 2. float
# 3. string
# 4. bool
# 5. tuple

# NU putem adauga liste/dictionare/seturi

valori = {1, 4,5, "Ana", True, (10, 11)}
# valori_gresit = {[1, 2], [3, 4]}
# print(valori_gresit)

# print(hash("ana"))
# print(hash((1, 2)))
# print(hash([1, 2]))

# Operatii cu seturi
# 1. Reuniune - toate valorile din ambele seturi, fara duplicate
a = {1, 2, 3}
b = {3, 4, 5}

rezultat = a.union(b)
# print(rezultat)

curs_java = {"Ana", "Florin", "Mihai"}
curs_python = {"Mihai", "Ioana", "Andrei"}
# studenti = curs_java.union(curs_python) # varianta cu union
studenti = curs_java | curs_python # varianta cu " | "
# print(studenti)
# print(curs_java)
# print(curs_python)

# 2. Intersectie: valori comune
a = {1, 2, 3}
b = {3, 4, 5}
# rezultat = a.intersection(b) # verifica valorile din primul set si le compara cu cele din al doilea, pe cele gasite in ambele le returneaza
rezultat = a & b
# print(rezultat)

# 3. Diferenta: difference() -> ce exista in primul set, dar nu exista in al doilea
a = {1, 2, 3}
b = {3, 4, 5}
diferenta = b.difference(a)
# print(diferenta)

studenti = {"Florin", "Andrei", "Mihai", "Maria"}
a_facut_tema = {"Mihai", "Maria"}

#fara_tema = studenti.difference(a_facut_tema)
fara_tema = studenti - a_facut_tema
# print(fara_tema)

# 4. Diferenta simetrica - valorile care apar intr-un set sau in altul, dar niciodata in ambele
a = {1, 2, 3}
b = {3, 4, 5}
rezultat = a.symmetric_difference(b)
# print(rezultat)

ieri = {"ana", "mihai", "george"}
azi = {"ana", "ioana", "george"}
# diferente = ieri.symmetric_difference(azi)
diferente = ieri ^ azi
# print(diferente)

# 5. subset -> issubset(): un set este subset daca toate elementele lui exista in alt set
a = {1, 2}
b = {1, 2, 3, 4}
# print(b.issubset(a))

acces_necesar = {"read", "write"}
acces_user = {"read", "write", "delete"}

# if acces_necesar.issubset(acces_user): # toate permisiunile necesare exista la user?
#     print("userul are accesul necesar")
# else:
#     print("userul nu are toate permisiunile")

# 6. superset - un set este superset daca include toate elementele altui set
a = {1, 2}
b = {1, 2, 3, 4}
# print(b.issuperset(a)) # setul b are toate valorile din a, deci b este superset pentru a

# 6. Seturi disjuncte: isdisjoint() -> doua seturi sunt disjuncte daca nu au niciun element comun
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))

