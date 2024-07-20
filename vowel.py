s=input()
num=0
vowels=['a','i','e','o','u']
for i in s:
    if i in vowels:
        num+=1
print(num)