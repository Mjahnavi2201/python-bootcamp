#program to sum all digits until we get single digits
def sum_of_digit(n):
    s1=0
    while(n>0):
        s1+=n%10
        n//=10
    return check(s1)
def check(n):
    if n<10:
        return n
    else:
        return sum_of_digit(n)
n=int(input())
print(check(n))