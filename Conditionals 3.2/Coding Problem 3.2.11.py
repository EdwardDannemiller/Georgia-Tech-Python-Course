cut = "Emerald"
clarity = "VS"
color = "E"
carat = 1.5
budget = 1500
preferred_cuts = ["Emerald", "Cushion", "Princess", "Oval"]

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Diamonds are typically evaluated according to four aspects:
# - Cut: The way the diamond is cut
# - Clarity: How clear or flawless the diamond is, rated
#   as F (the best), IF, VVS, VS, SI, or I (the worst)
# - Color: How colorless the diamond is, rated from "D" (the
#   best) to "Z" (the worst)
# - Carat: How large the diamond is, weighed in carats
#
#Cut is usually a matter of personal preference. Clarity,
#color, and carat are matters of value: the clearer, more
#colorless, and larger a diamond is, the greater its value.
#
#Imagine you're shopping for a diamond. You have your
#preferred cuts, and you have a budget in mind. You're shown
#a diamond whose characteristics are represented by the cut,
#color, clarity, and carat variables above. You'll buy the
#diamond if its cost is less than your budget, and if its
#cut is one of your preferred cuts.
#
#At this store, every diamond has a base cost of 100.
#
#For every color rating worse than "D", the cost decreases by
#2%. An "F" color diamond would be worth 0.96 * the diamond
#cost otherwise because "F" is two colors worse than "D".
#
#A diamond's value is doubled for every level of clarity above
#I. A "VVS"-clarity diamond is worth 8 * the diamond cost
#otherwise because "VVS" is three levels higher than I, and
#doubling its value three times raises its value by 8x total.
#
#After finding its price based on color and clarity, its price
#is multiplied by its weight in carats.
#
#Your program should print "I'll take it!" if you will buy the
#diamond, "No thanks" if you will not. To purchase it, its price
#must be less than your budget and its cut must be one of your
#preferred cuts.
#
#HINT: You can find the number of characters between two
#characters by using the ord() function. ord("E") - ord("D")
#is 1; ord("Z") - ord("D") is 22.
#
#HINT 2: We haven't covered lists, but we did cover how to
#see if an item is present in a list using the 'in' operator
#in chapter 2.3.


#Add your code here!
cost = 100
colorDiff = 1 - (0.02 * (ord(color) - ord("D")))
cost *= colorDiff

power = 0
if clarity == "SI":
    power = 1
elif clarity == "VS":
    power = 2
elif clarity == "VVS":
    power = 3
elif clarity == "IF":
    power = 4
elif clarity == "F":
    power = 5

cost *= (2 ** power)

cost *= carat

if (cut in preferred_cuts) and budget >= cost:
    print("I'll take it!")
else:
    print("No thanks")
