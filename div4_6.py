def check(arr):
 count=0
 for i in arr:
  if i%4==0 or i%6==0:
   count+=1
 return count
arr=list(map(int,input().split()))
print(check(arr))