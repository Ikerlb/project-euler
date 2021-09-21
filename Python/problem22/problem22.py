names=sorted(open('p022_names.txt',"r").read().replace('"',"").split(","))

def score(st):
	s=0
	for c in st:
		s+=(ord(c)-64)
	return s

scores=[score(names[i])*(i+1) for i in range(len(names))]

print(sum(scores))

