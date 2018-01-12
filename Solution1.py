"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""
def question1(original_string,sub_string):
    
    # check if original_string is a string
    if type(original_string) != str:
        return "Error: Input is not a string!"

    # check if sub_string is a string
    if type(sub_string) != str:
        return "Error: Input is not a string!"

    # check if original_string is not empty
    # and sub_string length is less than original_string
    if len(original_string) == 0 or len(original_string) < len(sub_string):
        return False

    # empty string is always a sub string of any string
    if len(sub_string) == 0:
        return True
    
    original_str_freq = char_frequency(original_string)
    sub_string_freq = char_frequency(sub_string)

    # iterates throug each chracter in the sub string
    # and checks if that character is present in the original string
    for character in sub_string:
        if character in original_string:
            #Compares frequency of each charecter 
            if sub_string_freq[str(character)] <= original_str_freq[str(character)]:
                flag = True
            else:
                return False
        else:
            return False
    return flag

# frequency of characters in each string are calculated
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

def test1():
    print "Test Case 1"
    print "Input - udacity,ad"
    print "Expected Output - True"
    print "Output - "+str(question1("udacity", "ad"))
    
    print "Test Case 2 - Edge Case - Input not a string"
    print "Input - 456,4.56"
    print "Expected Output - Error: Input is not a string!"
    print "Output - "+str(question1(456, 4.56))
    
    print "Test Case 3 - sub string longer than original string"
    print "Input - ad,udacity"
    print "Expected Output - False"
    print "Output - "+str(question1("ad", "udacity"))
    
    print "Test Case 4 - sub string equal to original string"
    print "Input - abcd,abcd"
    print "Expected Output - False"
    print "Output - "+str(question1("abcd", "abcd"))
    
    print "Test Case 5 - repeated substrings"
    print "Input - abcdabcdabcdabcdabcdabcdeabcd,abce"
    print "Expected Output - False"
    print "Output - "+str(question1("abcdabcdabcdabcdabcdabcdeabcd", "abce"))

testing()
