def fibo(n):
	(a,b)=1,1
	for i in range(n-1):
		(a,b)=b,a+b
	return a

n=1
while len(str(fibo(n)))<1000:
	n+=1

print(n)


# [phi**n / sqrt(5)]