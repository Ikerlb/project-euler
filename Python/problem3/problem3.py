from math import sqrt, floor

target=600851475143
n=target
#works sorta like a sieve
i=2
while n>1:
    while n%i==0:
        n=n/i
    i+=1
print(i-1)
