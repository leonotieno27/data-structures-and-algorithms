"""
used in
Computer File systems
BST used in sorted data for quick look ups, insertion and deletions
    .databases indexing and searching
    .autocomplete or search suggetsions
    .symbol tables in compilers
DOM: manipulation

Traversal Techniques
pre-order - top- left child - bottom - right child
post-order - left child- bottom, next bottom finishes top
breadth-first - top to bottom

"""
#each node can have  multiple children
class TreeNode:
    def __init__(self, value):
        """"Initialize a tree node with a value and an empty list of children"""
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Add a child node to current"""
        self.children.append(child_node)

    def display(self, level=0):
        """Display the tree structure """
        print(" " * level + str(self.value))
        for child in self.children:
            child.display(level + 1)
        
    def find(self, value):
        """Find a node in the tree with given value"""
        if self.value == value:
            return self
        for child in self.children:
            result = child.find(value)
            if result:
                return result
        return None
    
#building and Traversing a tree

if __name__ == "__main__":
    #root node
    root = TreeNode("Root")

    #child nodes
    child1 = TreeNode("child 1")
    child2 = TreeNode("child 2")
    child3 = TreeNode("child 3")

    #add children to root
    root.add_child(child1)
    root.add_child(child2)

    #add grandchildren
    child1.add_child(TreeNode("Child 1.1"))
    child1.add_child(TreeNode("Child 1.2"))
    child2.add_child(TreeNode("Child 2.1"))
    child3.add_child(TreeNode("Child 3.1"))

    #display tree
    print("Tree Structure")
    root.display()

    #find specific node
    print("\nFinding  'Child 1.1'")
    node = root.find("Child 1.1")
    if node:
        print(f"Node found: {node.value}")
    else:
        print("Node not found.")


"""BINARY TREES"""
#each tree has atmost two children
class BinaryTreeNode:
    def __init__(self, value):
        """"Initialize a binary tree node with a value and left/right children"""
        self.value = value
        self.left = None
        self.right = None


    def insert_left(self, value):
        """"insert a value as a left child"""
        self.left = BinaryTreeNode(value)

    def insert_right(self, value):
        """"insert value as right child"""
        self.right = BinaryTreeNode(value)

    def display(self, level=0):
        """Display the binary tree structure in a readable format"""
        print(" " * level +  str(self.value))
        if self.left:
            self.left.display(level + 1)
        if self.right:
            self.right.display(level + 1)

#building a binary tree
if __name__ == "__main__":
    #create root node
    root = BinaryTreeNode("Root")

    #add left and right children
    root.insert_left("Left Child")
    root.insert_right("Right Child")

    #Add grandchildren
    root.left.insert_left("Left Grandchild")
    root.left.insert_right("Right Grandchild")
    root.right.insert_left("Right's child's Left Grandchild")

    #Display the bianry tree
    print("Binary Tree Structure:")
    root.display()

#implementing traversals
class Node:
    """A class to represent a node in binary tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Binary tree with traversal methods"""
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node, result):
        """Preorder Traversal (Root -> Left -> Right)"""
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        """Postorder Traversal (Left ->Right ->Root)"""
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)

    def breadth_first_traversal(self):
        """Breadth-First Traversal (Level Order Traversal)"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)

            #enqueue left and right children if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result
    
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root. right.right = Node(7)

    #preorder Traversal
    preorder_result = []
    tree.preorder_traversal(tree.root, preorder_result)
    print("Preorder Traversal:", preorder_result)

    #postorder Traversal
    postorder_result = []
    tree.postorder_traversal(tree.root, postorder_result)
    print("Post-order Traversal: ", postorder_result)

    #breadth-first Traversal
    bfs_result = tree.breadth_first_traversal()
    print("Breadth-Firsr Traversal:", bfs_result)
