'''LIST:

list is a collection of ordered elements
list is a mutable datastructure(mutable-can be changed)
Syntax:-
	LIST_NAME=[obj1,obj2,obj3,...objn]
Operations:-

'''
mobiles=['iphone','samsung','vivo']
print(mobiles[1])
mobiles.insert(2,'oppo') #oppo is inserted at 2nd position
print(mobiles)
mobiles.pop() #oppo is deleted
print(mobiles)
mobiles.append('oppo') #oppo is added at the end
print(mobiles)
mobiles.remove('samsung') #removes samsung
print(mobiles)
mobiles.pop(1) #deletes index 1 elements
print(mobiles)
mobiles[1]='blackberry'
print(mobiles)
mobiles.clear() #to empty list
print(mobiles)
mobiles=['iphone','samsung','vivo','oppo','nothing']
print(mobiles[True]) #true value is 1
print(mobiles[False]) #false value is 0
#to print all elements with serial no
count=1
for ele in mobiles:
    print(count,ele)
    count+=1
#to print even indexing elements
for i in range(0,len(mobiles)):
    if i%2==0:
        print(mobiles[i])
#reversing even elements
for i in range(0,len(mobiles)):
    if i%2==0:
        rev=mobiles[i]
        print(rev[::-1])
    else:
        print(mobiles[i])
#reversing odd elements
for i in range(0,len(mobiles)):
    if i%2==1:
        rev=mobiles[i]
        print(rev[::-1])
    else:
        print(mobiles[i])