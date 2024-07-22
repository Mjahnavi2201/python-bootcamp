n=2397
m=3
'''
output:
	592721
  If even digit add with m
  If odd digit multiply with multiply
'''
n=str(n)
for i in n:
    if int(i)%2==0:
        print(int(i)+m,end='')
    else:
        print(int(i)*m,end='')