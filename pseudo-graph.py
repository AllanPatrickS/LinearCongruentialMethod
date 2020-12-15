import random
import math
from matplotlib import pyplot as plt

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

    rand = list(map(trunc, rand))
    cl = list(map(trunc, cl))

    print('\nMétodo random\n')
    print(rand)
    print('\nMétodo congruente linear\n')
    print(cl)
    bins = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    plt.hist(rand, bins, histtype='bar', width=0.8)
    plt.legend()
    plt.xlabel('Intervalos')
    plt.ylabel('Frequência')
    plt.title('Randeom')
    plt.show()

    plt.hist(cl, bins, histtype='bar', width=0.8)
    plt.legend()
    plt.xlabel('Intervalos')
    plt.ylabel('Frequência')
    plt.title('Congruente Linear')
    plt.show()


def trunc(n):
    return math.trunc(n*10) / 10


handle(rand(100), mcl(2138928109318, 590, 289018098098, 100, 100))
handle(rand(1000), mcl(2138928109318, 590, 289018098098, 100, 1000))
