from math import sqrt,floor

hexagonal=lambda x:x*(2*x-1)

def is_triangular(x):
    n=sqrt(2*x+0.25)-0.5
    return n==floor(n) 

def is_pentagonal(x):
    n=(1+sqrt(24*x+1))/3
    return floor(n)==n

i=1
h=hexagonal(i)
hpt=h
while hpt<=40755:
    h=hexagonal(i)
    if is_pentagonal(h):
        hpt=h
    i+=1
print(hpt)
