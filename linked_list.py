class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
first=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
first.next=second
second.next=third
third.next=fourth
fourth.next=None
head=first
while head.next!=None:
    print(head.data)
    head=head.next