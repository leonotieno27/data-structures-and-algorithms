"""
used in
Computer File systems
BST used in sorted data for quick look ups, insertion and deletions
    .databases indexing and searching
    .autocomplete or search suggetsions
    .symbol tables in compilers
DOM: manipulation

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

