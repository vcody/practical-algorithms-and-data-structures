# Class OOP version
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

# List implementation

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

def insert_left(root, child_val):
    subtree = root.pop(1)
    if len(subtree) > 1:
        root.insert(1, [child_val, subtree, []])
    else:
        root.insert(1, [child_val, [], []])
    return root

def insert_right(root, child_val):
    subtree = root.pop(2)
    if len(subtree) > 1:
        root.insert(2, [child_val, [], subtree])
    else:
        root.insert(2, [child_val, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root [1]

def get_right_child(root):
    return root[2]

root = [3, [], []]
insert_left(root, 4)
insert_left(root, 5)
insert_right(root, 6)
insert_right(root, 7)
left = get_left_child(root)
print(left) # [5, [4, [], []], []]

set_root_val(left, 9)
print(root) # [3, [9, [4, [], []], []], [7, [], [6, [], []]]]

insert_left(left, 11)
print(root) # ...
print(get_right_child(get_right_child(root))) # [6, [], []]