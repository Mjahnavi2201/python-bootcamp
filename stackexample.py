class StackExample:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def is_empty(self):
        return self.stack==[]
    def pop(self):
        if self.is_empty():
            print('Stack Underflow')
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            print(self.stack[-1])
    def display(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            for top in range(len(self.stack)-1,-1,-1):
                print(self.stack[top])
obj=StackExample()
obj.push(10)
obj.push('hi')
obj.push(30.0)
obj.peek()
obj.display()
obj.pop()
obj.pop()
obj.display()
obj.pop()
obj.pop()