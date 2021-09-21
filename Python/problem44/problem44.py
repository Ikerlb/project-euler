from math import sqrt,floor
#todo: memoize
pn=lambda n:(n*(3*n-1))//2

def is_pentagonal(x):
    n=(1+sqrt(24*x+1))/6
    return floor(n)==n

for s in range(3,10000):
    ps=pn(s)
    for k in range(s-1,0,-1):
        pk=pn(k)
        #print("ps",ps,"pk",pk,"ps-pk",ps-pk,"|2pk-ps|",abs(2*pk-ps))
        if is_pentagonal(ps-pk) and is_pentagonal(abs(2*pk-ps)):
            print(pk,ps-pk,abs(2*pk-ps))
             
