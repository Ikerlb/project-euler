def sols(n):
    res=set()
    for b in range(1,n//2):
        a=((n*n)-(2*n*b))/(2*n-2*b)
        if a==int(a):
            res.add(n-int(a)-b)
    return res

m=set()
p=0
target=1000
for i in range(2,target,2):
    r=sols(i)
    if len(r)>len(m):
        m=r
        p=i
print(m,p)
