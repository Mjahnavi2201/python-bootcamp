s1=input()
s2=''
for i in range(len(s1)-1,-1,-1):
   s2+=s1[i]
if s1==s2:
   print("It is a palindrome")
else:
   print("It is not a palindrome")
   
   