#123=>312=>231=>123 its easy to see there are as many rotations as there are digits

def rotate(s):
    l=list(s)
    ld=l.pop(-1)
    return "".join(([ld]+l))

def sieve(upto):
    l=[True]*upto
    l[0]=l[1]=False
    primes=set()
    for (i,isprime) in enumerate(l):
        if isprime:
            primes.add(str(i))
            for j in range(i*i,upto,i):
                l[j]=False
    return primes

target=1000000
primes=sieve(target)
res=set()

def rotations_are_prime(s):
    n=s
    for _ in range(len(s)-1):
        n=rotate(n)
        if n not in primes:
            return False
    return True

for s in primes:
    if rotations_are_prime(s):
        res.add(i)

