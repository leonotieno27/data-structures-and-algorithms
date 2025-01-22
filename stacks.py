"""
implements LIFO(Last IN First OUT)
use cases, web search history and undo
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        #check stack is empty
        return len(self.items) == 0
    
    def push(self, item):
        #add item on stack
        self.items.append(item)
    
    def pop(self):
        """remove item from stack"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """return number of items in the stack"""
        return len(self.items)

    def __str__(self):
        """Return a string represention of the stack"""
        return "Stack(" + ", ".join(str(item) for item in self.items) + ")"


if __name__ == '__main__':
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushing elements: ", stack)
    print("Top element:", stack.peek())
    print("Stack size:", stack.size())

    print("Popped element:", stack.pop())
    print("Stack after popping element:", stack)

    print("Is stack empty?", stack.is_empty())    
    
