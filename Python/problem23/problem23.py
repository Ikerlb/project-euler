import timeit
from math import sqrt
def dsum(n):
	s=1
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			s+=(i)
			if i!=n//i:
				s+=(n//i)
	return s

start_time = timeit.default_timer()
abundant={i for i in range(1,28123) if dsum(i)>i}

s=0
for i in range(1,28123):
    for j in abundant:
        if i-j in abundant:
            break
        elif (i<<1)>i:
            s += i
            break

print(timeit.default_timer() - start_time)
print(s)
