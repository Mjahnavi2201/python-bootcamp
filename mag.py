n=int(input())
org=n
sum1=0
while (n>0):
    sum1+=n%10
    n//=10
n=sum1
dig,rev=0,0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n//=10
pro=rev*sum1
if pro==org:
    print("MAGICAL")
else:
    print("NOT MAGICAL")