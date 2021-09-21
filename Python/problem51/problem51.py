import itertools

def sieve(upto):
    np=set()
    primes=[2]
    for i in range(3,upto,2):
        if i not in np:
            primes.append(i)
            for j in range(i*i,upto,i):
                np.add(j)
    return primes

primes=sieve(1000000)
sprime=set(primes)

def replace_digits(n,d,j):
    l=list(str(n))
    for i in d:
        l[i]=str(j)
    return int("".join(l))

def all_replaced_primes(n,d):
    res=[]
    for j in range(10):
        rd=replace_digits(n,d,j)
        if rd in sprime and len(str(n))==len(str(rd)):
            res.append(rd)
    return res

def check_number(n):
    ln=len(str(n))
    for j in range(2,ln):
        for i in itertools.combinations(range(ln),j):
            if len(all_replaced_primes(n,i))==8:
                print(n,i)
                return True
    return False

for p in primes:
    if check_number(p):
        break
