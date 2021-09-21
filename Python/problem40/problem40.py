#why does this fail?
#l={1,10,100,1000,100000,1000000}
#l={1,9,10,11,12,13,14,15,16,17}
#print(l)
#n=1
#r=1
#for i in range(1,1000000): 
#    for d in str(i):
#        n+=1
#        if n in l:
#            print(d)
#            r*=int(d)

target=1000000
s=""
i=1
while len(s)<target:
    s+=str(i)
    i+=1

d=[9,99,999,9999,99999,999999]
ds=[int(s[i]) for i in d]
print(ds)
