#print next character 
#s='abcdz'
#output:
# bcdea
s=input()
s1=''
for i in s:
    if i!='z' and i!='Z':
        s1+=chr(ord(i)+1)
    else:
        if i=='z':
            s1+='a'
        else:
            s1+='A'        
print(s1)