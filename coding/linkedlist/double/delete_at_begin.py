class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class doubleLL:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            print("Double linked list is empty")
        a = self.head
        while a is not None:
            print(a.data , end=" ")
            a = a.next

    def reverse_traverse(self):
        if self.head is None:
            print("Double linked list is empty")
        print()
        a = self.head
        while a.next is not None:
            a = a.next
            
        while a is not None:
            print(a.data,end=" ")
            a = a.prev
    
    def delete_at_begin(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None
        a.prev = None

node1 = Node(10)
dll = doubleLL()
dll.head = node1
node2 = Node(20)
node1.next = node2
node2.prev = node1
node3 = Node(30)
node2.next = node3
node3.prev = node2
node4 = Node(40)
node3.next = node4
node4.prev =node3
dll.traverse()
dll.reverse_traverse()
dll.delete_at_begin()
dll.traverse()
