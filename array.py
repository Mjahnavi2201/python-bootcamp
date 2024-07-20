#hacker rank array problem
list1=list(map(int,input().split()))
k=int(input())
first=list1[k-1:]
second=list1[:k-1]
print(first+second)
first.extend(second)
print(first)