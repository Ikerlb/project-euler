#key insights:
#   can only contain primes at starts
#   middle numbers can contain number 1
#   cannot start or end with 9
#   can only contain 5 on the start

def sieve(upto):
    primes={'2'}
    notprimes=set()
    for i in range(3,upto,2):
        if i not in notprimes:
            primes.add(str(i))
            for j in range(i*i,upto,i):
                notprimes.add(j)
    return primes

target=1000000
primes=sieve(target)
res=set()

def is_truncatable(s):
    for i in range(1,len(s)):
        p1=s[:len(s)-i]
        p2=s[i]
        if p1 not in primes or p2 not in primes:
            return False
    return True

res=[int(r) for r in primes if is_truncatable(r) and int(r)>7]
