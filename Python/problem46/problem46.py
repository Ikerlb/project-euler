from math import sqrt,floor,ceil
def is_prime(n):
    if n%2==0:
        return False
    for i in range(3,floor(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def goldbach(n):
    k=1
    for k in range(1,floor(((n/2)**(0.5)))+1):
    #while 2*(k**2)<=n:
        if is_prime(n-2*(k**2)):
            return True
        k+=1
    return False

n=9
while True:
    if is_prime(n):
        n+=2
        continue
    if not goldbach(n):
        print(n)
        break
    n+=2
