#draft: this is what we do.
#i=1
#level1=[1]
#while i<in*in+1
#leveli=list(range(level_i-1[-1]+1,i*i+1))
#sum+=leveli[-1]+leveli[-i-2]+leveli[-2*i-2]+leveli[-3*i-2]
#leveli=level_i-1
#lesgo

import time

start=time.time()
x=1001
i=1
leveli=[1]
s=1
while i*i<x*x:
    i+=2
    last=i*i
    for _ in range(4):
        s+=last
        last-=(i-1)
end=time.time()
print(end-start)
print(s)
