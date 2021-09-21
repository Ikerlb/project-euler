def recurring_cycle(d):
	mem={}
	value=1
	position=0
	recurrence=""
	while value not in mem:
		if value==0:
			return recurrence
		mem[value]=position
		value*=10
		value%=d
		position+=1
	length=position-mem[value]
	for _ in range(length):
		value*=10
		recurrence+=str(value//d)
		value%=d
	return recurrence

a=[(i,recurring_cycle(i)) for i in range(1,1000)]
sa=sorted(a,key=lambda x:len(x[1]))
print(sa[-1][0])