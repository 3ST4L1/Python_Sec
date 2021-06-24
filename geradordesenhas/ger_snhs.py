#!/usr/bin/python3

import random
import string


def tamanho():
    size = int(input('Size password: '))
    return size


def caracters():
    chars = string.ascii_letters + string.digits + '!@#$%&*/:-=ç'
    return chars


def grd_ss(c, t):
    rnd = random.SystemRandom()
    print(''.join(rnd.choice(c) for i in range(t)))


grd_ss(caracters(), tamanho())
