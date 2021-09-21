res=[]

def check(num,den):
    if num%10==0 and den%10==0:
        return
    ds=str(den)
    ns=str(num)
    for d in ns:
        if d in ds:
            nds=ds.replace(d,"",1)
            nns=ns.replace(d,"",1)
            if nds!='0' and (num/den)==int(nns)/int(nds):
                res.append((int(nns),int(nds)))


for num in range(10,100):
    for den in range(num+1,100):
        check(num,den) 


