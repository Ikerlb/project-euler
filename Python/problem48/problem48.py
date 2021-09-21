target=1000
ans=0
for i in range(1,target+1):
    ans+=i**i
print(str(ans)[-10:])
