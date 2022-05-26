#Write a function called wish_list. wish_list should have
#four parameters, in this order: 
#
# - a list of strings, representing a list of items on a
#   wish list
# - a string, representing a particular item
# - a float, representing the cost of this item
# - a float, representing your budget
#
#If the item is on the list and you can afford it (cost is
#less than or equal to budget), return the string,
#"You should buy a [item name]!", replacing [item name]
#with the string.
#
#If the item is on the list but you can't afford it,
#return the string, "You should save up for a [item name]!",
#replacing [item name] with the string.
#
#If the item is not on the list, you should return the
#string "You probably don't want to buy a [item name].",
#replacing [item name] with the string.
#
#HINT: You do not need a loop to solve this. You can use
#one, but you don't need one.


#Add your function here!
def wish_list(wishes, item, cost, budget):
    message = ''
    if not (item in wishes):
        message = "You probably don't want to buy a {0}.".format(item)
    elif cost > budget:
        message = "You should save up for a {0}!".format(item)
    else:
        message = "You should buy a {0}!".format(item)
    return message


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "You should save up for a bugle!"

wish_list_items = ["trumpet", "banjo", "tuba"]
selected_item = "bugle"
item_cost = 19.99
budget = 150.00

print(wish_list(wish_list_items, selected_item, item_cost, budget))


