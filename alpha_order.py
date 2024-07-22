#Arrange character in alphabet order
#ord()-converts char to ascii
#chr()-converts ascii to char
s=input()
for i in s:
    print(i,'->',ord(i)-96)