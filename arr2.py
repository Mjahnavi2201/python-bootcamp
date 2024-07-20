arr=[1,2,3,4,5]
k=2
'''first=arr[k+1:k-1:-1]
second=arr[:k-1]
print(first+second)'''
first=arr[-1:k:-1]
second=arr[:k+1]
print(first+second)