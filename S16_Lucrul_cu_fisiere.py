# -*- coding: utf-8 -*-

# Deschiderea fisierelor cu functia open()
# f = open(path, mode='r', encoding=None) # sintaxa
# path -> (sir de caractere) calea catre fisier(relativa sau absoluta)
# mode -> (sir de caractere optinal) modul in care deschidem fisierul('r', 'w', 'a', 'rb' etc)

# Moduri deschidere fisier
# 1. r -> read/citire - fisierul trebuie sa existe, altfel apare eroarea FileNotFoundError
# 2. w -> write/scriere - daca fisierul exista, este golit(sters); altfel, se creeaza automat
# 3. a - -> append/deschidere pentru adaugare - Scrie la finalul fisierului, daca nu exista, se creeaza
# 4. x - -> exclusive creation(creeaza doar daca nu exista), daca exista deja: returneaza eroarea FileExistsError
# 5. b -> fisiere binare
# 6. t -> mod text. Este mod implicit, nu e obligatoriu sa fie specificat
# + -> adauga permisiuni de citire si scriere simultan(r+ ; w+ ; a+)

# Deschidere pentru citire
# f = open('test.txt', 'r')
# Dupa ce deschidem un fisier, putem parcurge continutul in mai multe feluri
# 1. read() -> returneaza tot continutul fisierului ca un sir de caractere
# continut = f.read() # string cu tot textul
# print(continut)
# f.close()
# 2. read(size) - citeste pana la dimensiunea specificata si returneaza
# f = open('test.txt', 'r')
# continut = f.read(6)
# print(continut)
# f.close()

# readline() - citeste o singura linie la apelare, inclusiv caracterul de newline \n de la final. intoarce sir gol cand ajunge la sfarsitul fisierului
# f = open('test.txt', 'r')
# linie1 = f.readline()
# linie2 = f.readline()
# print(linie1, linie2, sep='\n')
# f.close()

# readlines() - citeste toate liniile si le pune intr-o lista
# f = open('test.txt', 'r')
# linii = f.readlines()
# print(linii)
# f.close()

# Parcurgerea fisierului cu for
# f = open('test.txt', 'r')
# for linie in f:
#     print(linie)
# f.close()

# Scrierea in fisier cu "w"
# f = open('test3.txt', 'w')
# f.write("Continut nou\n")
# f.write("Inca o linie noua\n")
# f.close()

# context manager
with open('test3.txt', 'w') as wf:
    wf.write("Continut nou cu context manager\n")
    wf.write("Inca o linie noua\n")



