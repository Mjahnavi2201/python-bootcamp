'''RECURSION:

function calling itself
'''
'''
#factorial
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
n=int(input())
print(fact(n))
'''
'''
#sum of natural numbers
def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)
n=int(input())
print(sum_n(n))  
'''
'''
#finding nth fibonacci series
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
'''