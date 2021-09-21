def is_pandigital(s):
    r=set("123456789")
    return set(s)==r and len(s)==9

res=set()

#we have several options here.
#it can be one digit 2 or 3
#if it is a 4 digit number, it must be higher than 5000 and less than 10k.

#1 digit
for n in range(1,10000):
    c=str(n)
    i=2
    while len(c)<9:
        c=c+str(n*i)
        i+=1
    if is_pandigital(c):
        res.add(c)
