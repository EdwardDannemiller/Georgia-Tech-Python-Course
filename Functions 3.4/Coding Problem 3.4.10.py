#Write a function called what_season. what_season should
#have two parameters: the first a string representing
#a month, and the second an integer representing a day.
#
#what_season should return "Spring" if the date is in
#Spring, "Summer" if it's in Summer, "Fall" if it's in
#Fall, and "Winter" if it's in Winter.
#
#For this problem, we define those seasons as follows:
#
# - Spring starts March 20.
# - Summer starts June 21.
# - Fall starts September 22.
# - Winter starts December 21.
#
#So, March 20 to June 20 would be Spring; June 21 to
#September 21 would be Summer; September 22 to December
#20 would be Fall; and December 21 to March 19 would be
#Winter.


#Add your code here!
def what_season(month, day):
    if (month == "April") or (month == "May"):
        return ("Spring")
    if (month == "July") or (month == "August"):
        return ("Summer")
    if (month == "October") or (month == "November"):
        return ("Fall")
    if (month == "January") or (month == "February"):
        return ("Winter")
    
    if (month == "March"):
        if (day >= 20):
            return ("Spring")
        else:
            return("Winter")
    if (month == "June"):
        if (day >= 21):
            return ("Summer")
        else:
            return("Spring")
    if (month == "September"):
        if (day >= 22):
            return ("Fall")
        else:
            return("Summer")
    if (month == "December"):
        if (day >= 21):
            return ("Winter")
        else:
            return("Fall")
    
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print Winter, Spring, Summer, and Fall in that order.
print(what_season("December", 25))
print(what_season("June", 15))
print(what_season("June", 23))
print(what_season("September", 27))

