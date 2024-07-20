'''DICTIONARIES:

dictionaries are mutable datastructure
it has key and pairs
keys cannot be repeated i.e keys are unique but values can be
Syntax:-
    DICT_NAME={key1:value,key2:value2...keyn:valuen}
'''
menu={
    'egg_bir':150,
    'egg_rice':100,
    'egg_curry':50,
    'pan_bir':70
    }
print(menu['pan_bir'])
menu['fruit_salad']=60 #to add
print(menu)
menu['pan_bir']=80 #to update
print(menu)
menu.pop('pan_bir') #to delete
print(menu.keys()) #to print keys
print(menu.values()) #to print values
#to print key and value in key->value
for k,v in menu.items():
    print(k,'->',v)
#to print key and value in key->value with sno
count=1
for k,v in menu.items():
    print(count,k,'->',v)
    count+=1