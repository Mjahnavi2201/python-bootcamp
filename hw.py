'''
n=500 #range(1-n)
#combinations of 2,4,8
#equal no. of 2's,4's and 8's
#no. of 2's > 0
Output:-
248
284
482
428
4
'''
def check(num):
    num=str(num)
    twos=num.count('2')
    fours=num.count('4')
    eights=num.count('8')
    return twos==fours==eights and twos>0
def increment(n):
    count=0
    for num in range(1,n+1):
        if check(num):
            print(num)
            count+=1
    return count
n=int(input())
print(increment(n))