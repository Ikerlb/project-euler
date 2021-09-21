#deterime last digit
#we need a number for which
from functools import reduce

fact=lambda x: reduce(lambda y,z:y*z,range(1,x+1))

facts=[1]+[fact(i) for i in range(1,10)]

def get_max_d():
    i=1
    while len(str((facts[9])*i))!=i:
        i+=1
    return i

d=get_max_d()
res=[]

def digits_list(n):
    digits=[]
    for c in str(n):
        digits.append(int(c))
    return digits

for i in range(3,facts[9]*d):
    if sum(map(lambda x:facts[x],digits_list(i)))==i:
        res.append(i)


