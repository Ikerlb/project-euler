import time

def is_prime(n):
    if n%2==0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i==0:
            return False
    return True

def sieve(upto):
    notprime=set()
    prime={2}
    for i in range(3,upto+1,2):
        if i not in notprime:
            prime.add(i)
            for j in range(i*i,upto+1,i):
                notprime.add(j)
    return prime

start=time.time()
ms=0
mb=0
ma=0
#b should be prime, means b should be positive
primes=sieve(1000)
for b in primes:
    for a in range(-b,1000,2):
        if not is_prime(a+b+1):
            continue
        n=0
        s=0
        nn=n*(n+a)+b
        if nn<2:
            continue
        while(is_prime(nn)):
            s+=1
            if s>ms:
                ms=s
                mb=b
                ma=a
            n+=1
            nn=n*(n+a)+b
            if nn<2:
                break
end=time.time()
print(ma,mb)
print(end-start)

