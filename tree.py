class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child
    
    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child

root = Node('a')
print(root.val) # 'a'
print(root.left) # 'None'

root.insert_left(Node('b'))
print(root.left) # Node object
print(root.left.val) # 'b'

root.insert_right(Node('c'))
print(root.right) # Node object
print(root.right.val)

root.right.val = 'hello'
print(root.right.val) # 'hello'

my_tree = [
    'a', # Root
    [
        'b', # Left sub-tree
        ['d', [], []],
        ['e', [], []]
    ],
    [
        'c', # Right sub-tree
        ['f', [], []],
        []
    ]
]

print(my_tree[1])
print(my_tree[2][0])

