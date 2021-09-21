#interesting solution i found

def sieve(upto):
    np=set()
    primes=[2]
    for i in range(3,upto,2):
        if i not in np:
            primes.append(i)
            for j in range(i*i,upto,i):
                np.add(j)
    return primes

def ocurrences(n,i):
    num=0
    si=str(i)
    for c in str(n):
        if c==si:
            num+=1
    return num

def replace_

primes=sieve(100000)



def n_replaces(n):
    for p in primes:
        d={ocurrences(p,i),i for i in range(3)}
        if n in d:
            
