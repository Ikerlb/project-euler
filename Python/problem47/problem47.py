from time import time
from math import sqrt,floor

def sieve(upto):
    notprimes=set()
    primes=[2]
    for i in range(3,upto,2):
        if i not in notprimes:
            primes.append(i)
            for j in range(i*i,upto,i):
                notprimes.add(j)
    return primes

def composite_primes(n):
    s=0
    d=2
    while d*d<=n:
        if not n%d:
            s+=1
            while not n%d:
                n//=d
        d+=1
    if n>1:
        s+=1 
    return s

def composite_primes2(n,primes):
    s=0
    i=0
    cp=2
    while cp*cp<=n:
        cp=primes[i]
        if not n%cp:
            s+=1
            while not n%cp:
                n=n//cp
        i+=1
    if n>1:
        s+=1
    return s

def composite_primes3(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return len(set(ans))

def pf1():
    start=time()
    n=2
    mn=4
    counter=1
    while counter!=mn:
        if composite_primes(n)==mn:
            counter+=1
        else:
            counter=0
        n+=1
    end=time()
    print(n-4,"Solution found in",end-start)

def pf2():
    start=time()
    n=2
    mn=4
    counter=1
    primes=sieve(1000000)
    ps=set(primes)
    while counter!=mn:
        if n in ps:
            counter=0
        elif composite_primes2(n,primes)==mn:
            counter+=1
        else:
            counter=0
        n+=1
    end=time()
    print(n-4,"Solution found in",end-start)

def pf3():
    start=time()
    n=2
    mn=4
    counter=1
    while counter!=mn:
        if composite_primes3(n)==mn:
            counter+=1
        else:
            counter=0
        n+=1
    end=time()
    print(n-4,"Solution found in",end-start)
            
