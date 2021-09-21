from math import sqrt,floor
import time
#number of digits of multiplicand multiplier and product has to be exactly 9. moreover they all must be different to each other and 0.
#if the number of digits in a number is given by floor(log10(n)) then the product floor(log10(n))*floor(log10(m))=log10(n+m) or floor(log10(n))*floor(log10(m))=n+m-1 

#thus we need numbers that satisfy the following:
#nd(m)+nd(n)+nd(n)+nd(m)=9 or m+n+n+m-1=9 first can't be satisfied, second means 2(n+m)=10=>n+m=5

def is_pandigital(m1,m2,n):
    s1=str(m1)
    s2=str(m2)
    s3=str(n)
    s=set(s1)|set(s2)|set(str(s3))
    return len(s1)+len(s2)+len(s3)==9 and len(s)==9 and '0' not in s

def method1():
    pds=set()
    for n in range(1,10):
        for m in range(1000,10000):
            p=n*m
            if is_pandigital(n,m,p):
                pds.add(p)

    for n in range(10,100):
        for m in range(100,1000):
            p=n*m
            if is_pandigital(n,m,p):
                pds.add(p)
    return pds

#alternatively
def method2():
    pds=set()
    for n in range(1234,9877):
        for j in range(1,floor(sqrt(n))):
            if n%j==0:
                s=set(str(n)+str(j)+str(n//j))
                if '0' not in s and len(s)==9:
                    pds.add(n)
    return pds


start1=time.time()
pds1=method1()
end1=time.time()
print("method 1 took",end1-start1)

start2=time.time()
pds2=method2()
end2=time.time()
print("method 2 took",end2-start2)

