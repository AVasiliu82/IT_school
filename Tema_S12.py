# 1. Creeaza catalogul unei clase. Ar trebui sa:
# - primim de la tastatura numele a 5 elevi
# - le salvam intr-o lista
# - afiseaza elevii care au numele mai lungi de 6 caractere

# 2. Se da o lista cu notele unui elev
# - afiseaza nota medie
# - afiseaza cea mai mica si cea mai mare nota
# - verifica daca elevul are vreo nota sub 5
# - creeaza o lista noua care contine doar notele mai mari decat 8
# tips: sum(), len(), min(), max()

# 3. Creeaza un program care simuleaza un cos de cumparaturi
# - adaugare produse in cos
# - afisare toate produsele
# - stergere produs dupa nume
# - verificare daca un produs exista in cos
# - afiseaza ultimul produs adaugat
# - goleste tot cosul
# - iesi din program

# bonus - exercitiu liste nested

# parcare mall - ai o parcare organizata pe randuri si coloane. Fiecare pozitie din matrice reprezinta un loc de parcare
parcare = [
    ["L", "L", "O", "L", "L"],
    ["O", "L", "L", "O", "L"],
    ["L", "L", "L", "L", "O"],
    ["O", "O", "L", "L", "L"]
]

# unde:
# L - Liber
# O - Ocupat
# Cerinta:
# - Afiseaza parcarea
# - Ocupa un loc. Daca este deja ocupat, afiseaza mesaj corespunzator. Validare pozitie(daca exista sau nu)
# - Elibereaza alt loc. Daca este deja liber, afiseaza mesaj corespunzator
# - Cauta primul loc liber. Daca parcarea este plina, afiseaza mesaj corespunzator
# - Numara cate locuri libere si cate locuri ocupate sunt
# - Afiseaza randul cu cele mai multe locuri libere
# - Iesire
# tips: while, def(), for, if/else