# i = 2
# print(type(i))
# f = 2.76457
# print(type(f))
# c = 0.5+1j
# print(type(c))
# print(float(i), int(f), c)
#
# a = 2>1
# print(a)
# print(type(a))
#
# b = 2.568568 >3
# print(type(b))
#
# znak = "A"
# print(type(znak))
#
# napis = "Ala ma kota"
# print(napis[::1])
# print(napis[::2])
# print(type(napis[::1]))
#
# zmienna = "127"*127
# print(type(zmienna))
#
# napis = "Ala ma kota a kot ma psa"
# liczba_calkowita = 2
# print(napis + str(liczba_calkowita))
#
# str1 = "Datatypes"
# str2 = "Fullstack"
# print(str1[3:6], str2[3:6])
# y = int(len(str1)*0.5)
# z = int(len(str2)*0.5)
# print(str1[y-1:y+2], str2[z-1:z+2])

# s1 = "Fullstack"
# s2 = "Python"
# y = int(len(s1)/2)
#
# print(s1[:y]+s2+s1[y:])

# s1 = "America"
# s2 = "Japan"
#
# x = s1[0] + s2[0]
# y = s1[-1]+s2[-1]
#
# z = s1[int(len(s1)/2)]+s2[int(len(s2)/2)]
# print(x+z+y)

# x = "Python"
# print(x[::-1])

# Jan = ("Jan", "Kowalski", 33)
# Janina = ("Janina", "Nowak", (21, 12,1978), "K")
# print(Jan, Janina)

# lista = [1, 2, 3, 4, -5, 6, -10]
# print(type(lista))

# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
#
# lista.insert(2, "zebra")
# print(lista)

# lista = ["Rafal", "Agata", "Michal", "Pawel", "Grzegorz", "Robert", "Aneta", "Tomasz", "Monika", "Klaudia", "Wiktor", "Kinga", "Marcin", "Tomasz", "Przemyslaw"]
#
# x = sorted(lista)
#
# print(len(x))
# print(x)

#   slownik
# tel = {}   #pusty
# tel = {'Maja':57657, 'Jasio':463557}
# tel["Ola"] = 3573577
# print(tel)
# del tel["Maja"]
# print(tel)
#
# tel = dict([('Jan', 4139277), ('Kazimierz', 4126327)])
# print(tel)

#   zbiór
# zbior = {"ala", "kot", 1, 2.89}
# print(zbior)
# randomowy wynik , nie powtaża elementów

# x = float(input("podaj liczbe 1 "))
# y = float(input("podaj liczbe 2 "))
# print(x/y)
# print(x//y)
# print(x%y)

# x = 8
# y = 15
# if x>3 or y%2==0:
#     print("conajmniej jeden z warunkow jest spelniony")
# elif x<=3 and y%2!=0:
#     print("zaden warunek nie zostal spelniony")

# x = False
# if not x:
#     print("warunek spełniony")
# else:
#     print("warunek niespełniony")

# kazda_wartosc = "test" and [123]
# print(kazda_wartosc)
# niepusta_wartosc = 0 or 0.0 or "" or [] or "test" or [123]
# print(niepusta_wartosc)

# x = float(input("podaj x "))
# print(x>3 and x<10)

# x = float(input("podaj x "))
# print(x>4 or x<3)


# x = float(input("podaj x "))
# print(not(x>3 and x<10))

# wartosc = 0
# wartosc = "warunek spełniony" if True else "warunek niespełniony"
# # if True: wartosc = "warunek spełniony"
# print(wartosc)

# nice = False
# nice = True
# personality = ("wredny", "mily") [nice]
# print("kot jest ", personality)

# string = 'Python'
# for litera in string:
#    print('litera:', litera)
# litera = string[0]
# print('litera:', litera)
# litera = string[1]
# print('litera:', litera)
# litera = string[2]
# print('litera:', litera)
# litera = string[3]
# print('litera:', litera)
# litera = string[4]
# print('litera:', litera)
# litera = string[5]
# print('litera:', litera)

# warzywa = ['marchew', 'kalafior', 'kapusta']
# for warzywo in warzywa:
#     print('warzywo:', warzywo)

# warzywa = ['marchew', 'kalafior', 'kapusta']
# i = 1
# for warzywo in warzywa:
#     print('warzywo:', i, warzywo)
#     i += 1

# print(4/7)
# print(4//7)
# print(4%7)

# lista = ["Rafal", "Agata", "Michal", "Pawel", "Grzegorz", "Robert", "Aneta", "Tomasz", "Monika", "Klaudia", "Wiktor", "Kinga", "Marcin", "Tomasz", "Przemyslaw"]
# lista.sort()
# i=0
# for t in lista:
#     if t[-1]=="a":
#         i=i+1
# print(i)

# print("Przykład range() w Pythonie")
# print("Uzyskaj liczby z zakresu od 0 do 5")
# for i in range(6):
#     print(i, end=', ')


# print(range(2, 11, 2))
#
# lista = list(range(2, 11, 2))
# print(lista)

# for i in range(5):
#     print(i)
# else:
#     print("gotowe")

# liczby = list()
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2
# print(liczby) # [2, 4, 6, 8, 10]

# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)

# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else: # normalny koniec pętli
#         print(n, 'jest liczbą pierwszą')

# for num in range(1, 20):
#     if not num % 2:
#         print("kolejna liczba parzysta ", num)
#         continue
#     print("kolejna liczba: ", num)

# x = int(input("pierwsza liczba: "))
# y = int(input("druga liczba: "))
# if x>y:
#     z = y
# else:
#     z = x
# for l in range(z,0, -1,):
#     if x % l == 0 and y % l == 0:
#         print(x, " i ", y, "dzieli sie przez ", l)
#         break
#   do rozmyślenia

# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
# else:
#     Pass

# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
# else:

# a = "Python"
# b = 317
#
# print("a: {}, b: {}".format(a, b))
# b, a = a, b
# print("a: {}, b: {}".format(a, b))
#  for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else: # normalny koniec pętli
#         print(n, 'jest liczbą pierwszą')

# for numer in range(1500,2701):
#     if numer % 7==0 and numer % 5 ==0:
#         print(numer)

# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
# simple_function()
#
# def my_function():
#     return 3+3
#
# print(my_function())

# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#     # while len(wynik) < n: # gdy chcemy ilość wyników
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
#
# x = fibbonaci_numbers(10)
# print(x)

# def ciag_znakow(x): # liczy ciąg znaków w stringu x
#     a = 0
#     for y in x:
#         a += 1
#     return a
#
# c = ciag_znakow("python")
#
# print(c)

# def suma_listy(x):      #suma wartości listy
#     a = 0
#     for i in x:
#         a+=i
#     return a
#
# b = suma_listy([4, 8, 12, 4, 5])
# print(b)

# def iloczyn_listy(x):      #iloczyn wartości listy
#     a = x[0]
#     for i in x[1:]:
#         a*=i
#     return a
# c = iloczyn_listy([2, 4, 6,])
# print(c)

# def lista(x):       #największa wartość z listy
#     a = x[0]
#     for i in x[1:]: #aby uniknąć pustego obliczenia dodajemy [1:] do x
#         if i > a:
#             a = i
#     return a
#
#
# c = lista([-20, -4, -60, -8])
# print(c)

# def google(x):      #zlicza liczbę znaków (częstotliwość znaków) w ciągu tekstowym
#     a={}
#     for i in x:
#         k = a.keys()  #klucz .keys()
#         if i in k:
#             a[i] += 1
#         else:
#             a[i] = 1
#     return a
# z = google("maamoooth")
# print(z)

# def ciag(x):
#     a = 0
#     for i in x:
#         if len(i) >= 2 and i[0] == i[-1]:       # do rozpatrzenia
#             a += 1
#
#     return a
# print(ciag(["aba",567, "abc", "coc", 12221, 404,]))


# def funkcja_1(krotkas):     #sortuje według 2 elementu
#     return krotkas[1]
# def krotkas(x):
#     a = sorted(x, key=funkcja_1)
#     return a
# print(krotkas([(2, 5), (1,2), (3,5), (2, 3)]))

# def ciag (x):
#         if len(x)<2:
#             return ""   #return konczy instrukcje i nie trzeba dawac else
#         return x[:2] + x[-2:]   # aby działało wcięcie równe if
# print(ciag("Py"))

# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#     # while len(wynik) < n: # gdy chcemy ilość wyników
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik


# def silnia(n):
#     if n == 1:
#         return 1
#     return silnia(n-1)*n
#
# print(silnia(5))


# def ciag(x):
#     if x<=1:
#         return x
#     return ciag(x-1) + ciag(x-2)
#
# print(ciag(11))

# Wyjątki i obsługa błędów
# try:
#   ...
#   <linie kodu>
# except Exception as err:
#   <obsługa wyjątku>

# import sys      # przykladowy kod do op na pliku
# try:
#     f = open("plik.txt")
#     s = f.readline()
#     i = int(s.strip())  # Usuń spacje
#     print(i)
# except OSError as err:
#     print("Błąd systemu: {0}".format(err))
# except ValueError:
#     print("Nie można dokonać konwersji.")
# except:     # PEP 8: E722 nie używaj pustego 'except'
#     print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
#     raise

# x = -1
#
# if x < 0:
#     raise Exception("Przepraszamy, brak liczb poniżej zera")


# while True:       #pętla zwracająca wartość 1 ciągle
#     try:
#         x = int(input("podaj 1 liczbę: "))
#         y = int(input("podaj 2 liczbę: "))
#         print(int(x+y))
#         break
#     except ValueError:
#         print("błąd")

# a = int(input("podaj 1 liczbę: "))
# b = int(input("podaj 2 liczbę: "))
# try:
#     result = a / b
# except ZeroDivisionError:
#     result = "Nie można dzielić przez 0 "
# print(result)

# lista = ["Rafal", 5, 2.4]
#
# try:
#     msg = lista[4]
# except IndexError as err:
#     msg = "Jesteś poza zakresem listy" + " (" + str(err) + ") "
# print(msg)


# import TestR
# arg = TestR
# try:
#     f = open(arg, "r")
# except IOError:
#     "Nie można otworzyć pliku"
# else:
#     print("Ilość wierszy: " + len(f.readlines()))
#     f.close()

#
# import TestR
# plik = TestR
# try:
#     plik = open("TestR.py", "r")
#     plik.write("string Lorum Ipsum")
# except IOError:
#     print("cos poszlo nie tak")
# finally:
#     plik.close()

#   Praca na plikach

# f = open('write_file_name', 'w')  # starą zawartość zastępujemy nową
# f = open('append_file_name', 'a')
# f = open('read_file_name', 'r')
#
# f.read()
#
# f.readline()

# f.write('Witaj\n')
# value = 42
# f.write(value)
#
# >>>Traceback (most recent call last):
# >>> File "<stdin>", line 1, in <module>
# >>>TypeError: must be str, not int
#
# s = str(value)
# f.write(s)


# # Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# # Zamknij otwarty plik
# fo.close()

# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.

# fo = open("text.txt", "r")
# print(fo.read())


# 1) bez użycia instrukcji with
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()

# with open("file_path.txt", "w") as file:
#     file.write('hello world !')

# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze go na liście content_list.
# content_list to lista zawierająca przeczytane wiersze.

# with open("text.txt", "r") as file:
#     content_list = file.readlines()
# print(content_list)

# content_list = []       #   sposób z pętlą
# with open("text.txt", "r") as file:
#     for i in file:
#         content_list.append(i)
# print(content_list)

# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym

# with open("text.txt", "r") as file:
#     a = file.read()
#
# b = a.split()
# c = ""
# for n in b:
#     if len(n) > len(c):
#         c = n
# print(c)

#       funkcja znajdująca najdłuższe ciągi

# def longest_word(filename):
#     with open(filename, 'r') as infile:
#         words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]
#
#
# print(longest_word('text.txt'))

# Napisz program w Pythonie, który zapisze listę do pliku.

# lista = ["reas", "sefew", 2535, "wefwe"]
#
# with open("nowy_plik", "w") as file:    # tworzy nowy_plik
#     for i in lista:
#         file.write(str(i) +"\n")

# Napisz program w Pythonie, aby ocenić, czy plik jest zamknięty, czy nie.

# file = open("text.txt", "r")
# print(file.closed)
# if not file.closed:
#     file.close()
# print(file.closed)

#                           Zadanie
# Napisz program, który otworzy plik sonety.txt i sprawdzi liczbę słów w całym tekście
# Dodatkowo, napisz funkcję, która zlicza słowa tylko w co 7 linijce tekstu


    #   impotowanie

# import os
# os.system("dir")

# from time import sleep  #   z modułu time importujemy tylko funkcję sleep
# print("Dobranoc")
# sleep(2)
# print("dzien dobry")

# import time   # bez określania funkcji
# print("Dobranoc")
# time.sleep(2)     #   trzeba po kropce
# print("Dzień dobry")

# from time import *    # importuje wszystkie funkcje z modułu
# print("dobranoc")
# sleep(2)
# print("dzien dobry")

# import time
# print(dir(time))  #   wszystkie obiekty w module

# from math import sin, pi  #   import z modułu math funkcji sin i pi
# a = sin(pi/2)
# print(a)

# def lemon(l):   #   tworzy moduł fruit
#     print('Lemoniada nr', l)
#
# import fruit
# # from fruit import lemon
#
# fruit.lemon(5)
# # lemon(5)

#       funkcje anonimowe

# pitagoras = lambda a, b:  ((a * a) + (b * b)) ** 0.5
# print(pitagoras(3, 4))

# def c_sum(x, y):
#     return x + y
#
# l_sum = lambda x, y: x+y
#
# print(c_sum(3, 4))
# print(l_sum(3, 4))

#       Filtrowanie, aplikowanie, redukowanie

temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3
]
# wynik = list(filter(lambda x: x >= 40.0, temperatury))
# print(wynik)
# wynik_sort = sorted(wynik)
# print(wynik_sort)
#
# from statistics import mean   #srednia
# st_temp = mean(temperatury)
# print(st_temp)
#
# odch = list(map(lambda x: round(x - st_temp,1), temperatury))
# print(odch)

# from functools import reduce        #redukuje do jednej wartości
# nums = [1, 2, 3, 4, 5]      #   działanie reduce ((((1+2)+3)+4)+5)
# print(reduce(lambda a, b: a + b, nums))

        #       list comprehension
# szesciany = []
# for x in range(10):
#     szesciany.append(x**3)
# print(szesciany)

        #   lub

# szesciany = [x**3 for x in range(10)]   #   tworzenie listy
# print(szesciany)

# kwadraty = [el**2 for el in range(1, 102) if el % 2 != 0]
# print(kwadraty)

# zbior = {znak for znak in "abracadabra" if znak not in "abc"}
# print(zbior)
#
# tekst = "abracadabra"
# wystapienia = {znak: tekst.count(znak) for znak in tekst}
# print(wystapienia)
#
# c = {x: x**2 for x in (2, 4, 6)}  # {2: 4, 4: 16, 6: 36}
# print(c)
#
# list_comp = [x ** 0.5 for x in range(1, 11)]
# gene_expr = (x ** 0.5 for x in range(1, 11))
#
# for x in list_comp:
#     print(x)
# for x in gene_expr:
#     print(x)
#
# list_comp = [x ** 0.5 for x in range(1, 50000001)]
# sum = 0
# for x in list_comp:
#     sum += x
# print(sum)
#
# gene_expr = (x ** 0.5 for x in range(1, 50000001))
# # gene_expr nie obliczyło jeszcze tych milionów pierwiastków
#
# sum = 0
# for x in gene_expr:
#     # teraz już kolejne elementy wyrażenia generatorowego są obliczane
#     sum += x
# print(sum)

