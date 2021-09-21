import time

def method1(target):
    s=0
    for i in range(3,target,3):
        s+=i
    for i in range(5,target,5):
        s+=i
    for i in range(15,target,15):
        s-=i
    print(s)

def method2(target):
    s=0
    for i in range(target):
        if i%3==0 or i%5==0:
            s+=i
    print(s)

def compare_methods(target):
    start1=time.time()
    method1(target)
    end1=time.time()
    print("Method 1 with input %s took %s" % (target,end1-start1))
    start2=time.time()
    method2(target)
    end2=time.time()
    print("Method 2 with input %s took %s" % (target,end2-start2))
