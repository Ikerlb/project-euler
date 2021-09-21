def is_palindrome(n):
    sn=str(n)
    return sn==sn[::-1]

#analysing further (checking the document), there is a neat way to improve.
#we know the resulting digit must be a 6 digit number as 111111 is not a prime number.
#then we know that this palindrome must be of the form 100000a+10000b+1000c+100c+10b+1a=100001a+10010b+1100c=11(9091a+910b+100c)
#since 11 is a prime number, it must come from either of the multiples.

m=1
for i in range(990,101,-1):
    for j in range(999,101,-1):
        if is_palindrome(i*j):
            m=max(i*j,m)
