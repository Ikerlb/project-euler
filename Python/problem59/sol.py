from itertools import product

with open("input.txt", "r") as f:
    txt = f.read()     
    # cyphertext
    ct = [int(n) for n in txt.split(",")]

def repeat(key):
    key = [ord(c) for c in key]
    i = 0
    while True:
        yield key[i]    
        i = (i + 1) % len(key) 


def _try(key, cyphertext):
    res = []
    for kc, cc in zip(cyphertext, repeat(key)):    
        res.append(kc ^ cc)    
    return res

 # 26 * 26 * 26 keys
# chances of all 
# cyphertext bytes
# being readable ascii
# are very slim
# so i'll do that 
# because i really dont
# want to use an english
# dictionary library 
# or api
l = [chr(i + ord('a')) for i in range(26)]
for k in product(l, repeat = 3):
    guess = _try(k, ct)
    if all(32 <= c <= 122 for c in guess):
        print(f"for key {k}, we got")
        print("".join(chr(c) for c in guess))
