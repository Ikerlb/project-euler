#for 1 only {1}
#for 2 only {1,1} {2}
#for 3 only {1,1,1} {1,2}
#for 4 only {1,1,1,1} {1,1,2} {2,2}
#for 5 only {1,1,1,1,1} {1,1,1,2} {1,2,2} {5}
#for 6 only {1,1,1,1,1,1} {1,1,1,1,2} {1,1,2,2} {1,5} {2,2,2}
#for 7 only {1,1,1,1,1,1,1} {1,1,1,1,1,2} {1,1,1,2,2} {1,2,2,2} {1,1,5} {2,5}
#for 8 only {1,1,1,1,1,1,1,1} {1,1,1,1,1,1,2} {1,1,1,1,2,2} {1,1,2,2,2} {1,1,1,5} {1,2,5} {2,2,2,2}
#for 9 only {1,1,1,1,1,1,1,1,1} {1,1,1,1,1,1,1,2} {1,1,1,1,1,2,2} {1,1,1,2,2,2} {1,1,1,1,5} {1,1,2,5} {1,2,2,2,2} {2,2,5}
#for 10 only {10*1} {8*1,2} {6*1,2,2} {4*1,2,2,2} 

#[   <=1     <=2     <=5     <=10    <=20    <=50    <=100   <=200]
#[1    1       1       1        1       1       1        1       1]
#[2    1       2       2        2       2       2        2       2]
#[3    1       2       2        2       2       2        2       2]
#[4    1       3       3        3       3       3        3       3]
#[5    1       3       4        4       4       4        4       4]

coins=[1,2,5,10,20,50,100,200]
target=200
mem=[[0 for i in range(len(coins))] for j in range(target+1)]
#optimize later
#only 1 way to make n with coins[0] (1)  
for j in range(len(coins)):
    mem[0][j]=1

for i in range(1,target+1):
    mem[i][0]=1

for i in range(1,target+1):
    for j in range(1,len(coins)):
        if i-coins[j]<0:
            mem[i][j]=mem[i][j-1]
        else:
            mem[i][j]=mem[i][j-1]+mem[i-coins[j]][j]

st=list(map(lambda x:"<="+str(x),coins))
print("\t"+"\t".join(st))
for i in range(1,target+1):
    print(str(i)+"\t"+"\t".join(list(map(str,mem[i]))))
