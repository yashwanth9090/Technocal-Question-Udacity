def question2(a):
    
    # check if input is a string
    if type(a) != str:
        return "Error: Input is not a string!"
   
    # length of the input string
    length = len(a)
    
    if length == 0:
        return "Error: Input string is empty!"
    
    if length == 1:
        return str(a)
    
    left_index = 0
    right_index = 0
    
    start = 0
    end = 1
    
    # iterates through each character and finds both even and odd palindrome
    for i in xrange(1, length):
        # left and right indexes represent center of palindromic substring of even length
        left_index = i - 1
        right_index = i
        # for every substring, starting at center towards left and right compares each character 
        while left_index >= 0 and right_index < length and a[left_index] == a[right_index]:
            if right_index - left_index + 1 > end:
                # keeps track of longest plaindromic substring
                start = left_index
                end = right_index - left_index + 1
            left_index -= 1
            right_index += 1
 
        # left and right indexes represent center of palindromic substring of odd length
        left_index = i - 1
        right_index = i + 1
        # for every substring, starting at center towards left and right compares each character 
        while left_index >= 0 and right_index < length and a[left_index] == a[right_index]:
            if right_index - left_index + 1 > end:
                # keeps track of longest plaindromic substring
                start = left_index
                end = right_index - left_index + 1
            left_index -= 1
            right_index += 1
            
    return a[start:start + end]


def test2():
    print "Test Case 1"
    print "Input - Empty string"
    print "Expected Output - Error: Input string is empty!"
    print "Output - "+str(question2(""))
    
    print "Test Case 2 - Edge Case"
    print "Input - 456"
    print "Expected Output - Error: Input is not a string!"
    print "Output - "+str(question2(456))
    
    print "Test Case 3 - single character"
    print "Input - a"
    print "Expected Output - a"
    print "Output - "+str(question2("a"))
    
    print "Test Case 4 - Two same characters"
    print "Input - aa"
    print "Expected Output - aa"
    print "Output - "+str(question2("aa"))
    
    print "Test Case 5 - Two different characters"
    print "Input - ab"
    print "Expected Output - a"
    print "Output - "+str(question2("ab"))
    
    print "Test Case 6 - Long string"
    print "Input - abcbaiojadoijaosdj"
    print "Expected Output - abcba"
    print "Output - "+str(question2("abcbaiojadoijaosdj"))
    
test2()