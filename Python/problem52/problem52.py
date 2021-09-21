def check(n,j):
    sn=str(n)
    for k in range(2,j+1):
        sk=str(k*n)
        if len(sn)!=len(sk) or set(sn)!=set(sk):
            return False
    return True

j=6
n=1
while not check(n,j):
    n+=1
print(n)
