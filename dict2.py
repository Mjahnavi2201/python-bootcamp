#frequency of numbers in arr
arr=[1,3,6,2,5,3,7,5,1]
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
'''
1:1+1
3:1+1
6:1
2:1
5:1+1
7:1
'''
#to print unique values
for k,v in d.items():
    if v==1:
        print(k)
#to print repeated values
for k,v in d.items():
    if v!=1:
        print(k)