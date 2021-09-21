import time

start=time.time()
amax=100
bmax=100

r=set()
for a in range(2,amax+1):
	for b in range(2,bmax+1):
            r.add(a**b)
end=time.time()
print(end-start)
print(len(r))
