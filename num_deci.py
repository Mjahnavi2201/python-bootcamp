#convert the num to decimal
def check(n):
    sum1,i=0,0
    while n>0:
        dig=n%10
        sum1+=(dig*(2**i))
        i+=1
        n//=10
    return sum1
n=101011
print(check(n))