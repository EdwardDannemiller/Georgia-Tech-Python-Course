#Write a function called mock. mock should take one
#parameter, a string. You may assume that the string will
#have only lowercase letters and spaces.
#
#Your function should return the same string, but any letter
#at an even index should be converted to uppercase.
#
#For example: mock("abcd efgh ijkl") would return
#"AbCd eFgH IjKl".
#
#Remember, you can use the ordinal function ord() to get the
#number associated with a single letter. For example,
#ord("a") returns 97. The number associated with lowercase
#letters is always 32 larger than the number associated with
#the equivalent uppercase letter. ord("a") is 97, and
#ord("A") is 65. ord("z") is 122, and ord("Z") is 90.
#
#Remember, you can use the character function chr() to
#convert a number back to a letter. For example, chr(65) will
#return "A".
#
#HINT: Treat all characters the same initially, then worry
#about taking care of spaces afterwards.


#Write your function here!
def mock(aString):
    evenIndex = aString[::2]
    oddIndex = aString[1::2]
    evenUpper = evenIndex.upper()
    counter = 0
    result = ''
    for i in aString:
        if ((counter % 2) == 0):
            result += evenUpper[0]
            evenUpper = evenUpper[1:]
        else:
            result += i
        counter += 1
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "AbCd eFgH IjKl".

print(mock("abcd efgh ijkl"))



