class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
def question5(ll, m):
    # check if input ll is a Node
    if type(ll) != Node:
        return "Input is not a Node!"

    # check if m is an integer
    if type(m) != int:
        return "m not an integer!"
    
    # initilize current_node and temp_node to head of ll
    current_node = ll
    temp_node = ll
    
    # traverse temp_node towards m elements
    for i in xrange(m):
        if temp_node.next is None:
            return "m is greater than ll length!"
        else:
            temp_node = temp_node.next
    
    # Current node points to head of ll
    # Temp node points to mth element from head
    # By traversing both nodes parallely untill temp reaches end of ll
    # current node reaches mth element from end
    while temp_node is not None:
        #print current_node.data
        current_node = current_node.next
        temp_node = temp_node.next
        
    return current_node.data

def test5():
    n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2
    
    print "Test Case 1"
    print "Input - ll not Node"
    print "Expected Output - Input is not a Node!"
    print "Output - "+str(question5(123, 111))
    
    print "Test Case 2 - Edge Case"
    print "Input - m > length of ll"
    print "Expected Output - m is greater than ll length!"
    print "Output - "+str(question5(n1, 6))
    
    print "Test Case 3 - Edge Case"
    print "Input - m not an integer"
    print "Expected Output - m not an integer!"
    print "Output - "+str(question5(n1, "1"))
    
    print "Test Case 4"
    print "Input - ll = n1 and m = 3"
    print "Expected Output - 3"
    print "Output - "+str(question5(n1, 3))
    
test5()