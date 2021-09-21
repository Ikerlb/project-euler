import time

txt=open('p67triangle.txt').read()
triangle=list(map(lambda x:list(map(int,x.split(' '))),txt.split('\n')[:-1]))

def propagate(n):
	for i in range(len(triangle[n-1])):
	    triangle[n-1][i]+=max(triangle[n][i],triangle[n][i+1])

for i in range(len(triangle)-1,0,-1):
	propagate(i)

print(triangle[0][0])

