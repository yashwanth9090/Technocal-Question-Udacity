class Tree_Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, n):
    # search if n is in the tree
    
    # Base Case
    if root is None or root.data == n:
        return root
 
    # if data is greater than root search right sub tree
    if root.data < n:
        return search(root.right,n)
   
    # if data is smaller than root search left sub tree
    return search(root.left,n)

def question4(r, n1, n2):
    # check if input r is a tree node
    if type(r) != Tree_Node:
        return "Input r not a Tree_Node!"

    # check if input n1 and n2 are integers
    if type(n1) != int:
        return "Input n1 not an integer!"
    if type(n2) != int:
        return "Input n2 not an integer!"

    # check if n1 and n2 are in the inptu tree
    if None == search(r, n1):
        return "Input n1 not in the tree!"
    if None == search(r, n2):
        return "Input n2 not in the tree!"
    
    current_node = findLCA(r, n1, n2)
    
    return current_node.data

def findLCA(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # finds in left tree if n1 and n2 smaller than root
    if(root.data > n1 and root.data > n2):
        return findLCA(root.left, n1, n2)
 
    # finds in left tree if n1 and n2 greater than root
    if(root.data < n1 and root.data < n2):
        return findLCA(root.right, n1, n2)
 
    return root

def test4():
    n1, n3, n5, n7 = Tree_Node(1), Tree_Node(3), Tree_Node(5), Tree_Node(7)
    n9, n11, n13, n15 = Tree_Node(9), Tree_Node(11), Tree_Node(13), Tree_Node(15)
    n2, n6, n10, n14 = Tree_Node(2), Tree_Node(6), Tree_Node(10), Tree_Node(14)
    n2.left, n2.right = n1, n3
    n6.left, n6.right = n5, n7
    n10.left, n10.right = n9, n11
    n14.left, n14.right = n13, n15
    n4, n12 = Tree_Node(4), Tree_Node(12)
    n4.left, n4.right = n2, n6
    n12.left, n12.right = n10, n14
    r = Tree_Node(8)
    r.left, r.right = n4, n12
    
    print "Test Case 1 - Edge Case"
    print "Input - r is not a Tree_Node"
    print "Expected Output - Input r not a Tree_Node!"
    print "Output - "+str(question4(123, 111, 111))
    
    print "Test Case 2 - Edge Case"
    print "Input - n1 not in the tree"
    print "Expected Output - Input n1 not in the tree!"
    print "Output - "+str(question4(r, -1, 5))
    
    print "Test Case 3"
    print "Input - n1 = 8 and n2 = 1"
    print "Expected Output - 8"
    print "Output - "+str(question4(r, 8, 1))
    
    print "Test Case 4"
    print "Input - n1 = 9 and n2 = 15"
    print "Expected Output - 12"
    print "Output - "+str(question4(r, 9, 15))
    
test4()

