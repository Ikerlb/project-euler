#i liked this one
#instead of searching through entire 10! search space,
#we construct backwards. start with multiples of 17 then find the ones with same suffix as this numbers prefix.
#can probably do better if you only add a digit to previous solution and check multiplicity.
#still happy with result

import time

def multiples(n):
    l=[str(num).zfill(3) for num in range(n,1000,n)]
    return [s for s in l if len(set(s))==len(s)]

def suffixed(m,s):
    return [n for n in m if n[1:]==s]

start=time.time()
primes=[2,3,5,7,11,13,17]

ms=[multiples(p) for p in primes]

possibles=ms[6]
for i in range(1,7):
    res=[]
    for s in possibles:
        sfxs=suffixed(ms[len(primes)-i-1],s[:2])
        for sfx in sfxs:
            res.append(sfx[0]+s)
    possibles=[r for r in res if len(set(r))==len(r)]

#finally, we concatenate possibles with 1 to 9 digits, remove non-pandigitals 
possibles=[d+p for p in possibles for d in '123456789' if d not in p]
end=time.time()
print("Result is:",sum(map(int,possibles)))
print("Program took: ",end-start)
