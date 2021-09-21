from math import floor,sqrt
pentagonal=lambda x:(x*(3*x-1))//2
d=1
flag=True
while flag:
    i=1
    pd=pentagonal(d)
    while True:
        n = (2*pd-i*(3*i-1))/(6*i)
        #if n is not an integer, try with the next i
        if floor(n)!=n:
            i+=1
            continue
        #since our function n(i) is decreasing, and pentagons start on 1
        if n<1:
            break
        pn=pentagonal(n)
        pni=pentagonal(n+i)
        sn=pn+pni
        s=floor((1+sqrt(1+24*sn))/6)
        if sn==pentagonal(s):
            print("pd",pd,"pni",pni,"pn",pn,"i",i,"n",n)
            flag=False
        i+=1
    d+=1
