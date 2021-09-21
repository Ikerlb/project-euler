def fact(n):
	prod=1
	for i in range(1,n+1):
		prod*=i
	return prod

def sdigits(n):
	s=0
	for c in str(n):
		s+=int(c)
	return s	
