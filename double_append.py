#double deque
from collections import deque
numbers=[1,2,3,4]
numbers=deque(numbers)
numbers.popleft() #to delete elements from left
numbers.pop() #to delete elements from right
print(numbers)