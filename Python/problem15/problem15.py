#project euler problem 15

#naive solution: dynamic programming
#sadly i'm going to simulate everything.

#we want all the different forms we can get to end by adding either one or n+1
#def ways(suma,mem,key="",counter=0):
#	if suma==end:
#		mem.add(key)
#		return
#	elif suma>end or counter>(2*n):
#		return
#	ways(suma+1,mem,key+"r",counter+1)
#	ways(suma+(n+1),mem,key+"d",counter+1)

def fact(n):
	p=1
	for i in range(1,n+1):
		p*=i
	return p

def res(n):
	return fact(2*n)//(fact(n)*fact(n))


#key insight, only being able to move to the right or down.

