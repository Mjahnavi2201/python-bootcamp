#print all 0's first
arr=[1,1,0,1,1,0,0]
zero=[]
one=[]
for i in arr:
    if i==0:
        zero.append(i)
    else:
        one.append(i)
zero.extend(one)
print(zero)