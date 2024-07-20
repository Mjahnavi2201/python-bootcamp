s=input()
count=0
vowels=['a','e','i','o','u']
for i in s:
  if i in vowels:
    count+=1
    break
if count==1:
    print('yes')
else:
    print('no')