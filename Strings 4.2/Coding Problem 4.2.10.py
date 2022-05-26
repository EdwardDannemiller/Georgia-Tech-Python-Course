#We've talked about ordinal numbers before, but they can
#mean something else: "ordinal" is also the term for numbers
#like 1st, 2nd, 3rd, 4th, etc.

#Write a function called to_ordinal. to_ordinal should
#take as input an integer greater than 0. to_ordinal should
#return a string of the ordinal of the integer (according to
#the above definition of ordinal).
#
#For example:
#
# to_ordinal(1) -> 1st
# to_ordinal(2) -> 2nd
# to_ordinal(3) -> 3rd
# to_ordinal(4) -> 4th
# to_ordinal(5) -> 5th
# to_ordinal(11) -> 11th
# to_ordinal(21) -> 21st
#
#Generally, ordinal numbers are always the original integer
#plus "th" _unless_ the original integer ended with 1 (in
#which case you add "st"), 2 (in which case you add "nd"),
#or 3 (in which case you add "rd")... except for 11, 12, and
#13, which still end in "th".


#Add your function below!
def to_ordinal(myInt):
    myStr = str(myInt)
    tens = myStr[-2:-1]
    ones = myStr[-1:]
    if tens == "1":
        return(myStr + "th")
    if ones == "1":
        return(myStr + "st")
    if ones == "2":
        return(myStr + "nd")
    if ones == "3":
        return(myStr + "rd")
    return(myStr + "th")
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#1st
#2nd
#3rd
#4th
#5th
#11th
#21st
print(to_ordinal(1))
print(to_ordinal(2))
print(to_ordinal(3))
print(to_ordinal(4))
print(to_ordinal(5))
print(to_ordinal(11))
print(to_ordinal(21))
