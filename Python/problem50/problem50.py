def sieve(upto):
    np=set()
    primes=[2]
    for i in range(3,upto,2):
        if i not in np:
            primes.append(i)
            for j in range(i*i,upto,i):
                np.add(j)
    return primes

#ut=100
#ut=1000
ut=1000000

def p50(ut):
    primes=sieve(ut)
    sprimes=set(primes)

    bs=0
    boff=0
    bidx=-1
    for i in range(len(primes)):
        s=0
        off=0
        while s<ut and i+off<len(primes):
            s+=primes[i+off]
            if s in sprimes and off>boff:
                bs=s
                boff=off
                bidx=i
            off+=1

    print("result is",bs,"expressed as the sum of the",boff+1,"consecutive primes starting with",primes[bidx])
