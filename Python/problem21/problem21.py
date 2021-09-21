#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

def d(n):
	div={1}
	for i in range(2,(n//2)+1):
		if n%i==0:
			div.add(i)
			div.add(n//i)
	return sum(div)

mem=[d(i) for i in range(10000)]

done=set()
s=0
for a in range(1,10000):
	if a!=mem[a]:
		if mem[a]<len(mem) and mem[mem[a]]==a:
				if not(a in done) and not(mem[a] in done):
					s=s+mem[a]+a
					done=done|{a,mem[a]}
