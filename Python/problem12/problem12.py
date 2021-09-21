import timeit

def get_nth_triangle(n):
	return int((n*(n+1))/2)

def brute_force_factors(n):
	factors=[1,n]
	i=2
	while i*i<=n:
		if n%i==0:
			q=n//i
			factors.append(i)
			if q!=i:
				factors.append(q)
		i+=1
	return factors

#get prime factorization
def prime_factorization(n):
	i=2
	factors={}
	while i*i<=n:
		if n%i:
			i+=1
		else:
			n//=i
			if factors.get(i) is None:
				factors[i]=1
			else:
				factors[i]+=1
	if factors.get(n) is None:
		factors[n]=1
	else:
		factors[n]+=1

	return factors

def number_of_factors(n):
	prod=1
	for val in prime_factorization(n).values():
		prod*=(val+1)
	return prod

def brute_force():
	start = timeit.default_timer()
	for i in range(15000):
		num=len(brute_force_factors(get_nth_triangle(i)))
		if num>=500:
			print i," ",num
			break;
	stop = timeit.default_timer()
	print 'Brute force: ', stop - start

def faster():
	start = timeit.default_timer()
	for i in range(15000):
		num=number_of_factors(get_nth_triangle(i))
		if num>=500:
			print i," ",num
			break;
	stop = timeit.default_timer()
	print 'Faster: ', stop - start

brute_force()
faster()