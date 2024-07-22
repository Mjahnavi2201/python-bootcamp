#task1
#find all combinations 'k' length substring of string 's'
s='abc'
k=2
for i in range(len(s)):
    if(i==len(s)-1):
        break
    print(s[i:i+k:])
print(s[i]+s[0:k-1:])