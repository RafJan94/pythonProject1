
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

# from statistics import mean
#
# sr_temp = mean(temperatury)
# print(sr_temp)
#
# odch = list(map(lambda x: round(x - sr_temp, 1), temperatury))
# print(odch)

# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(reduce(lambda a, b: a + b, nums))

# szesciany = []
# for x in range(10):
#     szesciany.append(x**3)
# print(szesciany)

# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
# r = fibbonaci_numbers(200)
# print(r)

# class Parrot:
#
#     species = "papuga"
#
#     # atrybuty instancji
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
#
# print(ascii(blu))
# print(bin(3))
# print(bin(-10))

#UZ

x = 885.04
y = 1000
print(x*1.23)
