def collatz(n):
	if n&1:
		return (3*n)+1
	return n>>1

def get_collatz_length(n):
	res=collatz(i)
	count=1
	while res!=1:
		res=collatz(res)
		count+=1
	return count

mem={}

for i in range(2,1000000):
	res=collatz(i)
	count=1
	while(res!=1):
		if mem.get(res) is not None:
			count+=mem[res]
			break
		res=collatz(res)
		count+=1
	mem[i]=count

max_key = max(mem, key=lambda k: mem[k])