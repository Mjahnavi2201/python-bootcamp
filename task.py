#task1
#find all combinations 'k' length substring of string 's'
s='abc'
k=2
for i in s:
    print(i[:k:])
print(s[-1]+s[0:k-1:])