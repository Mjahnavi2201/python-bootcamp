#Day3 Task-1:
'''
alice=[10,3,6]
bob=[12,3,4]
-count the greater than values of alice and bob
'''
alice=[10,3,6]       #list(map(int,input().split())) for dynamic inputs
bob=[12,3,4]         #list(map(int,input().split())) for dynamic inputs
a,b=0,0
for i in range(len(alice)):
    if alice[i]>bob[i]:
        a+=1
    elif alice[i]<bob[i]:
        b+=1
    else:
        continue
print('Alice:',a)
print('Bob:',b)