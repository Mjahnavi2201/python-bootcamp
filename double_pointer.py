#double pointer
arr=[1,2,3,4,5]
k,count=5,0
first=0
last=len(arr)-1
while first<last:
    if arr[first]+arr[last]==k:
        count+=1
        first+=1
        last-=1 
    elif arr[first]+arr[last]<k:
        first+=1
    else:
        last-=1    
print(count)