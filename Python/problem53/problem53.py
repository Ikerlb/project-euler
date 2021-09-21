def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

def c(n,r):
    return fact(n)//(fact(r)*fact(n-r))

res=set()

for n in range(1,101):
    for r in range(1,n):
        if c(n,r)>1_000_000:
            res.add((n,r))


