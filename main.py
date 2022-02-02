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
#
# s1 = "Fullstack"
# s2 = "Python"
# y = int(len(s1)/2)
#
# print(s1[:y]+s2+s1[y:])
#
# s1 = "America"
# s2 = "Japan"
#
# x = s1[0] + s2[0]
# y = s1[-1]+s2[-1]
#
# z = s1[int(len(s1)/2)]+s2[int(len(s2)/2)]
# print(x+z+y)
#
# x = "Python"
# print(x[::-1])
#
# Jan = ("Jan", "Kowalski", 33)
# Janina = ("Janina", "Nowak", (21, 12,1978), "K")
# print(Jan, Janina)
#
# lista = [1, 2, 3, 4, -5, 6, -10]
# print(type(lista))
#
# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
#
# lista.insert(2, "zebra")
# print(lista)
#
# lista = ["Rafal", "Agata", "Michal", "Pawel", "Grzegorz", "Robert", "Aneta", "Tomasz", "Monika", "Klaudia", "Wiktor", "Kinga", "Marcin", "Tomasz", "Przemyslaw"]
#
# x = sorted(lista)
#
# print(len(x))
# print(x)
#
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
#
#   zbiór
# zbior = {"ala", "kot", 1, 2.89}
# print(zbior)
# randomowy wynik , nie powtaża elementów
#
# x = float(input("podaj liczbe 1 "))
# y = float(input("podaj liczbe 2 "))
# print(x/y)
# print(x//y)
# print(x%y)
#
# x = 8
# y = 15
# if x>3 or y%2==0:
#     print("conajmniej jeden z warunkow jest spelniony")
# elif x<=3 and y%2!=0:
#     print("zaden warunek nie zostal spelniony")
#
# x = False
# if not x:
#     print("warunek spełniony")
# else:
#     print("warunek niespełniony")
#
# kazda_wartosc = "test" and [123]
# print(kazda_wartosc)
# niepusta_wartosc = 0 or 0.0 or "" or [] or "test" or [123]
# print(niepusta_wartosc)
#
# x = float(input("podaj x "))
# print(x>3 and x<10)
#
# x = float(input("podaj x "))
# print(x>4 or x<3)
#
#
# x = float(input("podaj x "))
# print(not(x>3 and x<10))
#
# wartosc = 0
# wartosc = "warunek spełniony" if True else "warunek niespełniony"
# # if True: wartosc = "warunek spełniony"
# print(wartosc)
#
# nice = False
# nice = True
# personality = ("wredny", "mily") [nice]
# print("kot jest ", personality)
#
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
#
# warzywa = ['marchew', 'kalafior', 'kapusta']
# for warzywo in warzywa:
#     print('warzywo:', warzywo)
#
# warzywa = ['marchew', 'kalafior', 'kapusta']
# i = 1
# for warzywo in warzywa:
#     print('warzywo:', i, warzywo)
#     i += 1
#
# print(4/7)
# print(4//7)
# print(4%7)
#
# lista = ["Rafal", "Agata", "Michal", "Pawel", "Grzegorz", "Robert", "Aneta", "Tomasz", "Monika", "Klaudia", "Wiktor", "Kinga", "Marcin", "Tomasz", "Przemyslaw"]
# lista.sort()
# i=0
# for t in lista:
#     if t[-1]=="a":
#         i=i+1
# print(i)
#
# print("Przykład range() w Pythonie")
# print("Uzyskaj liczby z zakresu od 0 do 5")
# for i in range(6):
#     print(i, end=', ')
#
#
# print(range(2, 11, 2))
#
# lista = list(range(2, 11, 2))
# print(lista)
#
# for i in range(5):
#     print(i)
# else:
#     print("gotowe")
#
# liczby = list()
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2
# print(liczby) # [2, 4, 6, 8, 10]
#
# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)
#
# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else: # normalny koniec pętli
#         print(n, 'jest liczbą pierwszą')
#
# for num in range(1, 20):
#     if not num % 2:
#         print("kolejna liczba parzysta ", num)
#         continue
#     print("kolejna liczba: ", num)
#
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
#
# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
# else:
#     Pass
#
# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
# else:
#
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
#
# for numer in range(1500,2701):
#     if numer % 7==0 and numer % 5 ==0:
#         print(numer)
#
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
#
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
#
# def ciag_znakow(x): # liczy ciąg znaków w stringu x
#     a = 0
#     for y in x:
#         a += 1
#     return a
#
# c = ciag_znakow("python")
#
# print(c)
#
# def suma_listy(x):      #suma wartości listy
#     a = 0
#     for i in x:
#         a+=i
#     return a
#
# b = suma_listy([4, 8, 12, 4, 5])
# print(b)
#
# def iloczyn_listy(x):      #iloczyn wartości listy
#     a = x[0]
#     for i in x[1:]:
#         a*=i
#     return a
# c = iloczyn_listy([2, 4, 6,])
# print(c)
#
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
#
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
#
# def ciag(x):
#     a = 0
#     for i in x:
#         if len(i) >= 2 and i[0] == i[-1]:       # do rozpatrzenia
#             a += 1
#
#     return a
# print(ciag(["aba",567, "abc", "coc", 12221, 404,]))
#
#
# def funkcja_1(krotkas):     #sortuje według 2 elementu
#     return krotkas[1]
# def krotkas(x):
#     a = sorted(x, key=funkcja_1)
#     return a
# print(krotkas([(2, 5), (1,2), (3,5), (2, 3)]))
#
# def ciag (x):
#         if len(x)<2:
#             return ""   #return konczy instrukcje i nie trzeba dawac else
#         return x[:2] + x[-2:]   # aby działało wcięcie równe if
# print(ciag("Py"))
#
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
#
# def silnia(n):
#     if n == 1:
#         return 1
#     return silnia(n-1)*n
#
# print(silnia(5))
#
#
# def ciag(x):
#     if x<=1:
#         return x
#     return ciag(x-1) + ciag(x-2)
#
# print(ciag(11))
#
# Wyjątki i obsługa błędów
# try:
#   ...
#   <linie kodu>
# except Exception as err:
#   <obsługa wyjątku>
#
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
#
# x = -1
#
# if x < 0:
#     raise Exception("Przepraszamy, brak liczb poniżej zera")
#
#
# while True:       #pętla zwracająca wartość 1 ciągle
#     try:
#         x = int(input("podaj 1 liczbę: "))
#         y = int(input("podaj 2 liczbę: "))
#         print(int(x+y))
#         break
#     except ValueError:
#         print("błąd")
#
# a = int(input("podaj 1 liczbę: "))
# b = int(input("podaj 2 liczbę: "))
# try:
#     result = a / b
# except ZeroDivisionError:
#     result = "Nie można dzielić przez 0 "
# print(result)
#
# lista = ["Rafal", 5, 2.4]
#
# try:
#     msg = lista[4]
# except IndexError as err:
#     msg = "Jesteś poza zakresem listy" + " (" + str(err) + ") "
# print(msg)
#
#
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
#
#   Praca na plikach
#
# f = open('write_file_name', 'w')  # starą zawartość zastępujemy nową
# f = open('append_file_name', 'a')
# f = open('read_file_name', 'r')
#
# f.read()
#
# f.readline()
#
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
#
#
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
#
# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.
#
# fo = open("text.txt", "r")
# print(fo.read())
#
#
# 1) bez użycia instrukcji with
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()
#
# with open("file_path.txt", "w") as file:
#     file.write('hello world !')
#
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu i zapisze go na liście content_list.
# content_list to lista zawierająca przeczytane wiersze.
#
# with open("text.txt", "r") as file:
#     content_list = file.readlines()
# print(content_list)
#
# content_list = []       #   sposób z pętlą
# with open("text.txt", "r") as file:
#     for i in file:
#         content_list.append(i)
# print(content_list)
#
# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym
#
# with open("text.txt", "r") as file:
#     a = file.read()
#
# b = a.split()
# c = ""
# for n in b:
#     if len(n) > len(c):
#         c = n
# print(c)
#
#       funkcja znajdująca najdłuższe ciągi
#
# def longest_word(filename):
#     with open(filename, 'r') as infile:
#         words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]
#
#
# print(longest_word('text.txt'))
#
# Napisz program w Pythonie, który zapisze listę do pliku.
#
# lista = ["reas", "sefew", 2535, "wefwe"]
#
# with open("nowy_plik", "w") as file:    # tworzy nowy_plik
#     for i in lista:
#         file.write(str(i) +"\n")
#
# Napisz program w Pythonie, aby ocenić, czy plik jest zamknięty, czy nie.
#
# file = open("text.txt", "r")
# print(file.closed)
# if not file.closed:
#     file.close()
# print(file.closed)
#
#                           Zadanie
# Napisz program, który otworzy plik sonety.txt i sprawdzi liczbę słów w całym tekście
# Dodatkowo, napisz funkcję, która zlicza słowa tylko w co 7 linijce tekstu
#
#
#       impotowanie
#
# import os
# os.system("dir")
#
# from time import sleep  #   z modułu time importujemy tylko funkcję sleep
# print("Dobranoc")
# sleep(2)
# print("dzien dobry")
#
# import time   # bez określania funkcji
# print("Dobranoc")
# time.sleep(2)     #   trzeba po kropce
# print("Dzień dobry")
#
# from time import *    # importuje wszystkie funkcje z modułu
# print("dobranoc")
# sleep(2)
# print("dzien dobry")
#
# import time
# print(dir(time))  #   wszystkie obiekty w module
#
# from math import sin, pi  #   import z modułu math funkcji sin i pi
# a = sin(pi/2)
# print(a)
#
# def lemon(l):   #   tworzy moduł fruit
#     print('Lemoniada nr', l)
#
# import fruit
# # from fruit import lemon
#
# fruit.lemon(5)
# # lemon(5)
#
#       funkcje anonimowe
#
# pitagoras = lambda a, b:  ((a * a) + (b * b)) ** 0.5
# print(pitagoras(3, 4))
#
# def c_sum(x, y):
#     return x + y
#
# l_sum = lambda x, y: x+y
#
# print(c_sum(3, 4))
# print(l_sum(3, 4))
#
#       Filtrowanie, aplikowanie, redukowanie
#
# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3
# ]
# wynik = list(filter(lambda x: x >= 40.0, temperatury))
# print(wynik)
# wynik_sort = sorted(wynik)
# print(wynik_sort)
#
# from statistics import mean   #srednia
# st_temp = mean(temperatury)
# print(st_temp)
# #
# odch = list(map(lambda x: round(x - st_temp,1), temperatury))
# print(odch)
#
# from functools import reduce        #redukuje do jednej wartości
# nums = [1, 2, 3, 4, 5]      #   działanie reduce ((((1+2)+3)+4)+5)
# print(reduce(lambda a, b: a + b, nums))
#
#               list comprehension
# szesciany = []
# for x in range(10):
#     szesciany.append(x**3)
# print(szesciany)
#
#           lub
#
# szesciany = [x**3 for x in range(10)]   #   tworzenie listy
# print(szesciany)
#
# kwadraty = [element**2 for element in range(1, 102) if element % 2 != 0]
# print(kwadraty)
#
# zbior = {znak for znak in "abracadabra" if znak not in "abc"}
# print(zbior)
#
# tekst = "abracadabra"
# wystapienia = {znak: tekst.count(znak) for znak in tekst}
# print(wystapienia)
#
# c = {x: x**2 for x in (2, 4, 6)}       # {2: 4, 4: 16, 6: 36}
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
#
#   Utwórz funkcję lambda, która przyjmuje jeden parametr (a) i zwraca go
#
# x = lambda a: a
# print(x(5))
#
# Napisz program w Pythonie, aby utworzyć funkcję lambda,
# która dodaje 15 do podanej liczby przekazanej jako argument i zwraca to wynik. Następnie wydrukuj wynik.
#
# x = lambda a: a+15
# print(x(5))
#
# Utwórz funkcję lambda, która mnoży argument x przez argument y i zwraca to wynik. Następnie wydrukuj wynik.
#
# a = lambda x, y: x*y
# print(a(2, 4))
#
# Napisz program w Pythonie wsparcia sortowania listy krotek za pomocą lambda po drugim elemencie
#
# subject_marks = [('Język angielski', 88),
#                  ('Nauka',           90),
#                  ('Matematyka',      97),
#                  ('Nauki społeczne', 82)]
# print(sorted(subject_marks, key=lambda a: a[1]))
#
#   Napisz program w Pythonie, aby posortować za pomocą lambda listę słowników po kluczu model lub kolor.
#
# models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
#           {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
#           {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
#
# print(sorted(models, key=lambda a:a["kolor"]))
#
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg (str) zaczyna się od znaku ‘P’, używając lambda
# Podpowiedź: skorzystaj z funkcji (metody) startswith()
#
# string = "APython"
# y = lambda a: a.startswith("P")
# print(y(string))    #   lub bezpośrednio zdefiniować pod y
#
# Napisz program w Pythonie, aby wyodrębnić rok, miesiąc, dzień i godzinę za pomocą lambda
# Podpowiedź: skorzystaj z modułu datetime:
# now = datetime.datetime.now() - przypisuje do nowaktualną lokalną datę i godzinę.
# now.year - wyodrębnia i zwraca rok z now.
# now.month - wyodrębnia i zwraca miesiąc z now.
# now.day - wyodrębnia i zwraca dzień z now.
# now.time() - wyodrębnia i zwraca godzinę z now.
#
# import datetime
#
# teraz = datetime.datetime.now()
# rok = lambda a: a.year
# miesiac = lambda b: b.month
# dzien = lambda c: c.day
# czas = lambda d: d.time()
#
# print(rok(teraz))
# print(miesiac(teraz))
# print(dzien(teraz))
# print(czas(teraz))
#
#   lub w jednej linijce
# f = lambda x: (x.year, x.month, x.day, str(x.time()))
# print(f(now))
#
# Napisz program w Pythonie, aby sprawdzić, czy dany string jest liczbą, czy nie, używając lambda
# Podpowiedź: przydatna metoda to
# string.replace(oldvalue, newvalue, count)
# Składnia parametrów:
# oldvalue – Wymagany; ciąg do wyszukania
# newvalue – Wymagany; ciąg znaków, który ma zastąpić starą wartość
# count – Opcjonalny; liczba określająca, ile wystąpień starej wartości chcesz zastąpić; domyślnie są to wszystkie wystąpienia
#
# isdigit zwraca true jeśli wszystkie są liczbami
#
# x = "2.2"
# y = lambda a: a.replace(".", "", 1).isdigit()
# z = lambda j: y(j[1:]) if j[0] == "-" else y(j)
# print(z(x))

# Napisz program w Pythonie do filtrowania listy liczb parzystych i nieparzystych całkowitych za pomocą lambda i filter

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# wynik = list(filter(lambda x: x % 2 == 0, lista))
# print(wynik)

# Napisz program w Pythonie, aby znaleźć przecięcie dwóch podanych list za pomocą lambda i filter

# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
#
# czesc_wspolna = list(filter(lambda x: x in array_nums1,array_nums2))
# print(czesc_wspolna)

# Napisz program w Pythonie, aby policzyć parzyste i nieparzyste liczby w danej tablicy liczb całkowitych, używając lambda i filter

# array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
#
# wynik = list(filter(lambda x: x % 2 == 0, array_nums))
# print(len(wynik))
# nieparzyste = list(filter(lambda x: x % 2 != 0, array_nums))
# print(len(nieparzyste))

# Napisz program w Pythonie, aby znaleźć wartości o długości sześć na podanej liście za pomocą funkcji lambda i filter

# weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
#
# wynik = list(filter(lambda x: len(x) == 6, weekdays))
# print(wynik)

# lub

# wynik = (filter(lambda x: len(x) == 6, weekdays))
# for d in wynik:
#     print(d)

# Napisz program w Pythonie, aby znaleźć liczby podzielne przez dziewiętnaście lub trzynaście z listy liczb za pomocą lambda i filter

# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
#
# f2 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, nums))
# print(f2)

# Napisz program w Pythonie, aby znaleźć palindromy na podanej liście ciągów za pomocą lambda i filter
# Palindrom – wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# Przykładem palindromu jest: „kobyła ma mały bok”

# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
#
# palindrom = list(filter(lambda x: x == x[::-1] , texts))
# print(palindrom)

# Napisz program w Pythonie, który zsumuje długość imion z danej listy imion po usunięciu imion zaczynających się od małej litery
# Użyj funkcji lambda

# sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']
#
# imiona = list(filter(lambda x: x[0].isupper() and x[1:].islower(), sample_names))
# a = "".join(imiona)
# print(len(a))  # ((imiona, )) -> jednoelementowa krotka

# Napisz program w Pythonie podnoszący do kwadratu i sześcianu każdą liczbę z podanej listy liczb całkowitych, używając lambda i map

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# kwadrat = list(map(lambda x: x**2, nums))
# print(kwadrat)
# szescian  =  list(map(lambda x: x**3, nums))
# print(szescian)

# Napisz program w Pythonie, aby dodać dwie podane listy za pomocą map i lambda

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
#
# suma = list(map(lambda x, y: x +y, nums1, nums2))
# print(suma)

# Napisz program w Pythonie, który za pomocą funkcji lambdamnoży każdą liczbę z podanej listy przez określoną liczbę
# Wydrukuj wynik

# nums = [2, 4, 6, 9, 11]
# n = 2
#
# wynik = list(map(lambda x: x*n,nums,))
# print(wynik)

# Napisz program w Pythonie, który usuwa liczby dodatnie z podanej listy liczb
# Zsumuj liczby ujemne i wydrukuj wartość bezwzględną za pomocą tworzenia listy – ang. list comprehension
# Wydrukuj wynik

# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
#
# print(abs(sum([x for x in nums if x<0])))   # list comprehension

# Napisz program w Pythonie, aby zmienić kolejność liczb dodatnich i ujemnych w danej liście
# (najpierw wszystkie ujemne, potem wszystkie dodatnie) za pomocą tworzenia listy – ang. list comprehension

# array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
#
# print([x for x in array_nums if x<0 ] + [x for x in array_nums if x>0])

# Napisz program w Pythonie, aby:
# Znaleźć liczby z podanego ciągu
# Zapisać je na liście
# Wyświetlić liczby w posortowanej formie
# Użyj funkcji tworzenia listy – ang. list comprehension, aby rozwiązać problem

# str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
#
# print(sorted([int(x) for x in str1.split() if x.isdigit()]))    #   przerabiamy na intiger x a nie cały list comprehension


    #   PYTHON OBJECT ORIENTED PROGRAMMING

# x = 4
# print(type(x))
# print(id(x)) # miejsce w pamięci komputera
#
# x = 5
# print(id(x))

# lst = [1, 2, 3]
# # print(id(lst))
# # print(type(lst))
# lst[0] = 2
# print(type(lst))
# print(lst)

# x = 4.5
# print(x.is_integer())
# x = 4.0
# print(x.is_integer())


# f = open("test.txt", "w")
# print(type(f))
# print(f.closed)
# f.close()
# print(f.closed)

# numbers = [6, 9, 3, 1]
# print(numbers)
# print(sorted(numbers))
# numbers.sort()
# print(numbers)

# x = 4.0
# print(x)
# print(type(x))
# print(x.real)
# print(type(x.real))
# print(x.is_integer())
# print(type(x.is_integer))

    #   KLASY

# class NazwaKlasy:
#     def nazwa_metody(self, argument1, argument2):   # musi być we wcięciu aby była metoda - w przeciwnym wypadku wychodzi funkcja
#         print(argument1)
#         print(argument2)
# obiekt = NazwaKlasy()
# obiekt.nazwa_metody("arg1", "arg2") # argument self jest domniemywany - nie musimy go podawać (podstawia się automatycznie obiekt, który wywołał metodę)

# class MyClass:
#     """Dokumentacja Klasy"""    # dokumentacja klasy
#
# help(MyClass)

# class NazwaKlasy:
#     atrybut_pierwszy = "wartosc"
#     atrybut_drugi = 123.0

# class NazwaKlasy:
#     def __init__(self, trzeci):
#         self.atrybut_pierwszy = "Wartość"
#         self.atrybut_drugi = 123.0
#         self.atrybut_trzeci = trzeci

# class MyClass:
#     x = 5
#
# p1 = MyClass()
#
# print(p1.x)

# class Parrot:
#
#     # atrybut klasy
#     species = "ptak"
#
#     # atrybut instancji
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # metoda instancji
#     def sing(self, song):
#         return self.name + " śpiewa " + song
#
#     def dance(self):
#         return self.name + " teraz tańczy"
#
# # utworzenie instancji klasy Parrot
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
#
# # uzyskanie dostępu do atrybutów klasy
# print("Blu to", blu.__class__.species)
# print("Woo to również", woo.__class__.species)
# # za chwilę wytłumaczymy sobie dokładniej o co chodzi z __class__
#
# # uzyskanie dostępu do atrybutów instancji
# print(blu.name, "ma", blu.age, "lat")
# print(woo.name, "ma", woo.age, "lat")
#
# blu = Parrot("Blu", 10)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def my_func(self):
#         print("Czesc mam na imie " + self.name)
#
# p1 = Person("Jan", 36)
# p1.my_func()

# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age
#
#     def my_func(abc):
#         print("Cześć, mam na imię " + abc.name)
#
# p1 = Person("Jan", 36)
# p1.my_func()
#
# p1.age = 40
#
# print(p1.age)
#
# del p1  # słuzy do usuwania obiektów w całym Pythonie
#
# p1.my_func()

# Klasa o nazwie MyClass z atrybutem o nazwie x
# No to jeszcze raz! Utwórz klasę o nazwie MyClass z atrybutem o nazwie x = 5.
# Teraz użyj klasy o nazwie MyClass do stworzenia obiektu.
# Utwórz obiekt o nazwie p1 i wydrukuj wartość x

# class MyClass:
#     x = 5
#
# p1 = MyClass()
# print(p1.x)


# class KontoBankowe:
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
# jk = KontoBankowe("Jan Kowalski", 1000)
#
# jk.info()
# jk.wplac(2000)
# jk.wyplac(2500)
# jk.info()
# jk.stan = 0
# jk.info()

# lasa (class) dotycząca wyimaginowanego inwentarza odrzutowca jest już dla Was zdefiniowana.
# Również instancja tej klasy Jets jest stworzona i przypisana do zmiennej first_item. Wydrukuj name z first_item.

# class Jets:
#
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
#
# a= first_item.name
# print(a)

# Tym razem wydrukuj origin z first_item.


# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
# a=first_item.name
# b= first_item.origin
#
#
# print(a,b)

# Utwórz klasę Vehicle z atrybutami instancji max_speed i mileage.
# Stwórz obiekt i w trakcie inicjacji przypisz jego atrybutom (odpowiednio) wartości 240 i 18.
# Wydrukuj te atrybuty.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# obiekt = Vehicle(240, 18)
#
# print(obiekt.mileage, obiekt.max_speed)

# Utwórz klasę Car z dwoma atrybutami instancji:
# .color, który przechowuje nazwę koloru samochodu jako ciąg testowy (str)
# .mileage, który przechowuje liczbę kilometrów przejechanych przez samochód jako liczbę całkowitą (int)
# 7:50
# Następnie utwórz instancję dwóch obiektów Car - niebieski samochód mający 20 000 kilometrów przebiegu i czerwony samochód mający 30 000 kilometrów przebiegu - i wydrukuj ich kolory oraz przebiegi. Twój wynik powinien wyglądać następująco:
# Niebieski samochód ma 20,000 kilometrów przebiegu.
# Czerwony samochód ma 30,000 kilometrów przebiegu.

# class Car:
#     def __init__(self, color, kilometry):
#         self.color = color
#         self.kilometry = kilometry
#
# Niebieski = Car(color = "niebieski", kilometry = 20000)
# Czerwony = Car(color = "czerwony", kilometry = 30000)
#
# # print(Niebieski.color, "samochód ma ", Niebieski.kilometry, " kilometrów przebiegu")
# # print(Czerwony.color, "samochód ma ", Czerwony.kilometry, " kilometrów przebiegu")
#
# for pojazdy in (Niebieski, Czerwony):   # używając pętli
#     print(pojazdy.color, pojazdy.kilometry)
#
# Stwórz nowe instancje od pierwszej do szóstej pozycji w tej kolejności: F14, SU 33, AJS37, Mirage 2000, Mig 29, A10.
# Możesz sprawdzić Podpowiedź 1, aby sprawdzić origin.

# Wskazówka 1
# SU33: Rosja
# AJS37: Szwecja
# Mirage2000: Francja
# F14: USA
# Mig29: ZSRR
# A10: USA

# Możesz utworzyć instancje w następujący sposób:
# first_item=Jets(name, country)

# class Jets:
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#     def samolot(self, drugi):
#         print(self.name, self.origin)
#         print(drugi.name, drugi.origin)
#
#
# first_item= Jets(name="F14",country="USA")
# second_item=Jets(name="SU33",country="Rosja")
# third_item=Jets(name="AJS37",country="Szwecja")
# fourth_item=Jets(name="Mirage 2000",country="Francja")
# fifth_item=Jets(name="Mig 29",country="ZSRR")
# sixth_item=Jets(name="A10",country="USA")
#
#
# # first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
# # third_item.samolot(second_item)
#
# # print(first_army)
#
# # for ajet in (first_item, second_item, third_item, fourth_item, fifth_item, sixth_item):
# #     ajet.samolot(first_item) #   jako drugi argument pobiera first_item
#
# jet_list = [Jets("F14", "USA"), Jets("SU33", "Rosja"), Jets("AJS37", "Szwecja")]
# for jet in jet_list:
#     jet.samolot(jet)    # dubluje bo w def są dwa printy


# Dodaj kolejny atrybut o nazwie „quantity” do metody inicjalizacji (zwykle nazywanej konstruktorem lub __init__).
# Następnie zdefiniuj przypisanie tego atrybutu do atrybutu self.quantity wewnątrz konstruktora.
# Następnie utwórz 2 instancje dla: F14 i Mirage2000 z ilościami 87 i 35.

# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
# Następnie musisz przypisać ten parametr do atrybutu self, aby istniało sensowne połączenie między parametrem a atrybutem.

# Możesz dodać parametr quantity do konstruktora w następujący sposób:
# def __init__(self, name, country, quantity):
#
#     self.name = name
#     self.origin = country
#     self.quantity = quantity
# Następnie musisz przypisać ten parametr do atrybutu self, aby istniało sensowne połączenie między parametrem a atrybutem.

# Możesz tworzyć instancje klasy Jets jak poniżej:
# first_item=Jets("F14","USA",87)
# second_item=Jets("Mirage2000","France",35)

