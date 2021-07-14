class Stack:
    def __init__(self):
        self._items = []
    
    def is_empty(self):
        return not bool(self._items)
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)

test_stack = Stack()

print(test_stack.size())
print(test_stack.is_empty())

test_stack.push('apple')

print(test_stack.size())
print(test_stack.is_empty())