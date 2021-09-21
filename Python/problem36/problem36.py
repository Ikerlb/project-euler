#function to get number of leading zeros to add, based on trailing zeros the number has
def with_leading(s):
    ntz=0
    for d in reversed(s):
        if d!='0':
            return s.zfill(ntz+len(s))
        ntz+=1

def is_palindrome(s):
    r=s[::-1]
    return s==r

def is_dec_bin_palindromic_leading(n):
    ld=with_leading(str(n))
    lb=with_leading("{:b}".format(n))
    return is_palindrome(ld) and is_palindrome(lb)

def leading_zeros_sol(target):
    s=set()
    for i in range(1,target):
        if is_dec_bin_palindromic_leading(i):
            s.add(i)

    print(sum(s))

def is_dec_bin_palindromic(n):
    return is_palindrome(str(n)) and is_palindrome("{:b}".format(n))

def sol(target):
    s=0
    for i in range(1,target,2):
        if is_dec_bin_palindromic(i):
            s+=i
    print(s)
