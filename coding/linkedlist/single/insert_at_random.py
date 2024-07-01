class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SinglyLL:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            print('Singly Linked list is Empty')
        else:
            a = self.head
            while a is not None:
                print(a.data , end=" ")
                a = a.next
    
    def insertion_at_specific(self,data,position):
        print()
        node_specific = Node(data)
        a = self.head
        for i in range(1,position - 1):
            a = a.next
        node_specific.next = a.next
        a.next = node_specific
        

n1 = Node(10)
sll = SinglyLL()
sll.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
sll.traverse()
sll.insertion_at_specific(3,4)
sll.traverse()