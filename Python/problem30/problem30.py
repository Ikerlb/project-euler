import time

def get_max_d(p):
    i=1
    while len(str((9**p)*i))!=i:
        i+=1    
    return i

start=time.time()
res=set()
p=5
maxd=get_max_d(p)
maxn=(9**p)*maxd
minn=2
for i in range(minn,maxn):
    s=0
    for d in str(i):
        s+=int(d)**p
    if s==i:
        res.add(i)

end=time.time()
print(end-start)
print(sum(res))

