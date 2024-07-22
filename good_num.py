#count good no.s in arr
'''
arr=[35,9,1] #output: 2
res=low cube + high cube
low=1
floor(),ceil()
'''
import math
arr=[35,9,1,65,126] 
c=0
res=0
for i in arr:
    low=1
    high=math.floor(math.cbrt(i))
    while low<high:
        res=(low**3)+(high**3)
        if res!=i:
            low+=1
        else:
            c+=1
            break
print(c)
    