#to print fibanocii series upto n
def fibanocii(n):
    first,second=0,1
    print(first,second,end=' ')
    count=2
    while count<n:
        third=first+second
        print(third,end=' ')
        first,second=second,third
        count+=1
n=int(input())
fibanocii(n)       