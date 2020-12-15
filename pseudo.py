import random
import math


def rand(n):
    pseudo = []
    for i in range(1, n+1):
        x = random.random()
        pseudo.append(x)
    return pseudo


def mcl(a, c, m, x0, n):
    pseudo = []
    if n < 1:
        return pseudo
    x1 = (a*x0 + c) % m
    x1 = x1 / m
    pseudo.append(x1)
    for i in range(2, n+1):
        x = (a*pseudo[i-2] + c) % m
        x = x / m
        pseudo.append(x)
    return pseudo


def handle(rand, cl):

    rand = map(trunc, rand)
    cl = map(trunc, cl)

    print('\nMétodo random\n')
    print(list(rand))
    print('\nMétodo congruente linear\n')
    print(list(cl))


def trunc(n):
    return math.trunc(n*10) / 10


handle(rand(100), mcl(2138928109318, 590, 289018098098, 100, 100))