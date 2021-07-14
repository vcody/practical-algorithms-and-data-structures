class Stack:
    def __init__(self):
        self._items = []
    
    def is_empty(self):
        return not bool(self._items)
    '''
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]
    '''
    # Also works
    def pop(self):
        return self._items.pop(0)

    def push(self, item):
        self._items.insert(0, item)
    
    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)
