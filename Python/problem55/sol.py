def is_palindrome(n):
    s=str(n)
    return s==s[::-1]

def reverse(n):
    s=str(n)
    return int(s[::-1])

def lychrel(n):
    for i in range(1,50):
        n=n+reverse(n)
        if is_palindrome(n):
            return False
    return True

def num_of_lychrels(upto):
    total=0
    for i in range(1,upto):
        if lychrel(i):
            total+=1
    return total

