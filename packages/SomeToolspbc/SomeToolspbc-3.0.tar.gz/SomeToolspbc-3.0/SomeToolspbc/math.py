
import time

def add(*num):
    if type(num[0]) == int:
        a = 0
    else:
        a = ''
    for i in num:
        a += i
    return a


def strdel(a,b=[]):
    c = ''
    for i in range(len(a)):
        if not i in b:
            c += a[i]
    return c

def fib(nth=33):
    n1 = 0
    n2 = 1
    n3 = 0
    count = 2
    while count < nth:
        count += 1
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n3

def exchange(a,b):
    c = a
    a = b
    b = c
    return [a,b]

def random():
    a = time.perf_counter()
    a *= 7874
    a %= 89792
    a *= 791725
    a %= 789677
    a *= 89473
    return a
#print(random())

def randint(a=0,b=89073298):
    ab = random()
    ab %= b+1-a
    ab += a
    return int(ab)

randseed = 0
init = False

def randLinear(a,b,sets=time.perf_counter()):
    global init,randseed
    if not init:
        randseed = sets
        init = True
    randseed *= 8972135
    randseed %= 7893278
    randseed *= 7965219
    randseed %= 1895823
    randseed *= 78912
    randseed %= b-a
    randseed += a
    return randseed

#for i in range(100):
#    print(randLinear(0,100),randseed)
        
    





    
