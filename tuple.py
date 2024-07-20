'''TUPLE:

tuple is a immutable datastructure and is a collection of multiple data elements
it is similar to list but it doesnot have index and immutable
we can only fetch in tuple
Syntax:-
    TUPLE_NAME=(obj1,obj2...objn)
'''
student=(101,'Umer','cse','Hyderabad')
print(student)
#to change convert tuple to list
student=list(student)
student[2]='ece'
student.append('swec')
print(tuple(student)) #to print the data in tuple