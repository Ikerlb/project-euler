from itertools import permutations
from math import floor,sqrt


digits='123456789'

def is_prime(p):
    for i in range(2,floor(sqrt(p))):
        if p%i==0:
            return False
    return True

def largest_pp(s):
    m=0
    p=map(lambda x:int("".join(x)),permutations(s,len(s)))
    l=[n for n in p if is_prime(n)]
    return -1 if l==[] else max(l)

for i in range(5,8):
    print(i,largest_pp(digits[:i]))
