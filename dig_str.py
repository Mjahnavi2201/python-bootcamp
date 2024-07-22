'''
input:
    s='a1b2c3d492nm45'
output:
    12349245abcdnm
-print all digits before all string is same order    
'''
s='a1b2c3d492nm45'
dig=''
s1=''
for i in s:
    if i.isdigit():
        dig+=i
    else:
        s1+=i
print(dig+s1)