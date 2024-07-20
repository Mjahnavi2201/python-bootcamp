s1=input()
s2=''
for i in range(len(s1)-1,-1,-1):
    s2+=s1[i]
if s1==s2:
    print("PALINDROME")
else:
    print("NOT PALINDROME")