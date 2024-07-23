#Balanced Brackets
#use stack
#from collections import stack
s='{[()]}' #balanced
open_brackets=['(','[','{']
stack=[]
for i in s:
    if i in open_brackets:
        stack.append(i)
    else:
        if i==')' and stack[-1]=='(':
            stack.pop()
        elif i=='}' and stack[-1]=='{':
            stack.pop()
        elif i==']' and stack[-1]=='[':
            stack.pop()
        else:
            continue
if stack==[]:
    print("Balanced")
else:
    print("Unbalanced")