f=open('words.txt','r')
words=f.read().replace("\"","").split(",")
msize=max(map(len,words))
numbers=set()
res=set()

n=0
i=1
while(n<25*msize):
    n=(i*(i+1))>>1
    numbers.add(n)
    i+=1

for w in words:
    s=sum(map(lambda x:ord(x)-64,w))
    if s in numbers:
        res.add(w)
