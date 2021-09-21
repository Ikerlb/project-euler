from time import time

def sieve(upto):
    np=set()
    primes=[2]
    for i in range(3,upto,2):
        if i not in np:
            primes.append(i)
            for j in range(i*i,upto,i):
                np.add(j)
    return primes

def is_permutation(n,m):
    sm=str(m)
    for c in str(n):
        if c in sm:
            sm=sm.replace(c,"",1)
        else:
            return False
    return True

start=time()
nd=4
primes=[i for i in sieve(10**nd) if i>=10**(nd-1)]
ps=set(primes)

i=0
for i in range(2,(10**nd)//3+1,2):
    for p in primes:
        if p+i in ps and is_permutation(p,p+i):
            if p+2*i in ps and is_permutation(p,p+2*i):
                print(i,"->",p,p+i,p+2*i)
end=time()
print("result took",end-start)
