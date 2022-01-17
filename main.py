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
#         if len(i) >= 2 and i[0] == i[-1]:       # do naprawy
#             a += 1
#
#     return a
# print(ciag(["aba",567, "abc", "coc", 12221, 404,]))

