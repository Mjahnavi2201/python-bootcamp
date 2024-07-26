#remove duplicate words
s='hello world hello world good morning good afternoon'
#method1
l1=s.split()
res=''
for i in l1:
    if i not in res:
        res+=i+' '
print(res)
#method2
d={}
res=''
for i in l1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if v>=1:
        res+=k+' '
print(res)