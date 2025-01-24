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




