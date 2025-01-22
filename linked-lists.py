"""Singly linked list"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        #add node at end of the linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Add a node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def delete_with_value(self, data):
        """Delete first node of the specified value"""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def print_list(self):
        """Print entire linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.print_list()
ll.delete_with_value(10)
ll.print_list()


"""Doubly linked list"""
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None        