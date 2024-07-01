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
    
    def delete_at_end(self):
        print()
        a = self.head
        while a.next.next is not None:
            a = a.next
        a.next = None
    
    # Another Method to delete node at end
    def delete_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        

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
sll.delete_at_end()
sll.traverse()
sll.delete_end()
sll.traverse()