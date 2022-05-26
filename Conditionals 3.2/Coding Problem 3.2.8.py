grade = 82
curve = 8

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Professor Burdell is grading final exams. Based on the
#class average, he has established a curve, whose value is
#given in the variable curve above.
#
#Then, for each individual student, he wants to send a
#personal message based on their grade. Their grade is the
#sum of the value of grade and the value of curve, but it
#cannot be greater than 100; if the curve takes them above
#100, their grade is 100.
#
#Prof. Burdell then wants to send one of the following
#messages, depending on the student's final grade:
#
# - If the total grade 90 to 100, the message would state:
#   "Congratulations! Your final grade is [their grade], an A."
# - If the total grade is 80 to 89, the message would state:
#   "Good job! Your final grade is [their grade], a B."
# - If the total grade is 70 to 79, the message would state:
#   "Not bad! Your final grade is [their grade], a C."
# - If the total grade is 60 to 69, the message would state:
#   "You passed! Your final grade is [their grade], a D."
# - If the total grade is under 60, the message would state:
#   "It's just one grade. Your final grade is [their grade], an F."
#
#[their grade] should be the result of adding grade and curve,
#but should not be greater than 100.


#Add your code here!
curvedGrade = grade + curve
if curvedGrade > 100:
    curvedGrade = 100

if curvedGrade >= 90:
    print("Congratulations! Your final grade is {0}, an A.".format(curvedGrade))
elif curvedGrade >= 80:
    print("Good job! Your final grade is {0}, a B.".format(curvedGrade))
elif curvedGrade >= 70:
    print("Not bad! Your final grade is {0}, a C.".format(curvedGrade))
elif curvedGrade >= 60:
    print("You passed! Your final grade is {0}, a D.".format(curvedGrade))
else:
    print("It's just one grade. Your final grade is {0}, an F.".format(curvedGrade))
