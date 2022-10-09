# задача 1. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

N = int(input("Введите число: "))


def primfacs(N):
    i = list()
    j = 2
    while j <= N:
        if (N % j) == 0:
            i.append(j)
            N = N / j
        else:
            j += 1
    return i


print(f"Простые множители числа {N} приведены в списке: {primfacs(N)}")


# Задача 2: Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input("Введите числа через пробел:\n").split()))


def get_numbers(numbers):
    lst = []

    for number in numbers:
        if number in lst:
            continue
        else:
            lst.append(number)
    return lst


print(get_numbers(numbers))



# 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


from random import randint
import itertools

k = randint(2, 9)


def get_ratios(k):
    ratios = []
    for i in range(k + 1):
        ratios.append(randint(0, 11))
    while ratios[0] == 0:
        ratios[0] = randint(1, 11)
    return ratios


def get_polynomial(k, ratios):
    var = ['*x^'] * (k - 1) + ['*x']
    polynomial = []
    for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue=''):
        if a != 0:
            polynomial.append([a, b, c])
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('33_Polynomial.txt', 'w') as data:
    data.write(polynom1)

k = randint(2, 5)

ratios = get_ratios(k)
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('33_Polynomial2.txt', 'w') as data:
    data.write(polynom2)

# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

x = int(input('a = '))
y = int(input('b = '))


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


print('НОК:', lcm(x, y))


