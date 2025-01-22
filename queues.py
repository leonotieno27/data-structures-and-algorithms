"""
FIFO Fisrt in First out
use case: people waiting in line for tickets, restaurant waitlist, call queue
"""

class Queue:
    def __init__(self):
        """Initializing empty queue"""
        self.items = []

    def is_empty(self):
        """check if item is empty"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """addd item at ennd of list"""
        self.items.append(item)

    def dequeue(self):
        """remove and return item at the front of the queue"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0) #at index 0
    
    def peek(self):
        """return front item without removing it"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]
    
    def size(self):
        """return number of items in the queue"""
        return len(self.items)
    
    def __str__(self):
        """string representation of queue"""
        return "Queue(" + " <- ". join(str(item) for item in self.items) + ")"
    

if  __name__ == '__main__':
    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)

    print("Queue after enqueue operations:", queue)
    print("Front item:", queue.peek())
    print("Queue size:", queue.size())

    print("Dequequed item:", queue.dequeue())
    print("Queue after dequeue:", queue)

    print("Is queue empty?", queue.is_empty())

#collections dequeue
#optimized for faster append and pop operations than lists
#popleft() is more efficient than list.po(0)

from collections import deque

class Queue2:
    def __init__(self):
        """initialize a deque for the queue"""
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        
    def size(self):
        return len(self.items)
    
#example usage

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.dequeue())