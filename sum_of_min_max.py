#sum of all min digit
#sum of all max digit
#print the difference of the sums
def check(num,l1):
    s=str(num)
    min1=int(s[0])
    max1=int(s[0])
    for i in s:
        if int(i)>max1:
            max1=int(i)
        if int(i)<min1:
            min1=int(i)
    l1.append(min1)
    l1.append(max1)
    return l1
def difference(l1):
    sum1,sum2=0,0
    for i in range(len(l1)):
        if i%2==0:
            sum1+=l1[i]
        else:
            sum2+=l1[i]
    diff=abs(sum1-sum2)
    return diff  
'''    
n1=7823
n2=5489
n3=1384
l1=[]
check(n1,l1)
check(n2,l1)
check(n3,l1)
print(difference(l1))
'''
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    check(i,l1)
print(difference(l1))