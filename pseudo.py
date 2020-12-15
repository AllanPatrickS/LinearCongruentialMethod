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


def handle(rand, cl, n):

    rand = list(map(trunc, rand))
    cl = list(map(trunc, cl))

    print('\nMétodo random {}\n'.format(n))
    print(rand)
    print('\nMétodo congruente linear {}\n'.format(n))
    print(cl)


def trunc(n):
    return math.trunc(n*10) / 10


handle(rand(100), mcl(2138928109318.0, 590.0, 289018098098.0, 57.0, 100), 100)
handle(rand(1000), mcl(2138928109318.0, 590.0, 289018098098.0, 57.0, 1000), 1000)
