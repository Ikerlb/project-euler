target=4000000
s=0

def linear_nth_fibo(n):
    prev=1
    f=1
    for _ in range(n-1):
        prev,f=f,f+prev
    return f

i=2
r=0
while r<=target:
    r=linear_nth_fibo(i)
    i+=3
    s+=r

print(s-r)
