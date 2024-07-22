ch='*'
ch1=' '
n=int(input())
for i in range(1,n+1):
	print(ch*i)
print()
'''
*
**
***
****
*****
'''
for i in range(n,0,-1):
    print(ch*i)
print()
'''
*****
****
***
**
*
'''

for i in range(0,n):
    for j in range(0,n):
        if i==j or i+j==n-1:
            print(ch,end='')
        else:
            print(ch1,end='')
    print()
print()
'''
*   *
 * *
  *
 * *
*   *
'''
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(ch,end='')
        else:
            print(ch1,end='')
    print()
'''
*****
*   *
*   *
*   *
*****
'''
for i in range(1,n+1):
    if i==1 or i==n:
        print(ch*n)
    else:
        print(ch+ch1*(n-2)+ch)
'''
*****
*   *
*   *
*   *
*****
'''