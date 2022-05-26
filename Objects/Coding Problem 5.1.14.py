#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, \
                cheese = False, pico = False, corn = False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
    def set_meat(self, newMeat):
        validMeats = ("chicken", "pork", "steak", "tofu", False)
        if newMeat in validMeats:
            self.meat = newMeat
        else:
            self.meat = False
    def set_to_go(self, newToGo):
        validToGo = (True, False)
        if newToGo in validToGo:
            self.to_go = newToGo
        else:
            self.to_go = False
    def set_rice(self, newRice):
        validRice = ("brown", "white", False)
        if newRice in validRice:
            self.rice = newRice
        else:
            self.rice = False
    def set_beans(self, newBeans):
        validBeans = ("black", "pinto", False)
        if newBeans in validBeans:
            self.beans = newBeans
        else:
            self.beans = False
    def set_extra_meat(self, newExtraMeat):
        validExtraMeat = (True, False)
        if newExtraMeat in validExtraMeat:
            self.extra_meat = newExtraMeat
        else:
            self.extra_meat = False
    def set_guacamole(self, newGuac):
        validGuac = (True, False)
        if newGuac in validGuac:
            self.guacamole = newGuac
        else:
            self.guacamole = False
    def set_cheese(self, newCheese):
        validCheese = (True, False)
        if newCheese in validCheese:
            self.cheese = newCheese
        else:
            self.cheese = False
    def set_pico(self, newPico):
        validPico = (True, False)
        if newPico in validPico:
            self.pico = newPico
        else:
            self.pico = False
    def set_corn(self, newCorn):
        validCorn = (True, False)
        if newCorn in validCorn:
            self.corn = newCorn
        else:
            self.corn = False
    def get_meat(self):
        return self.meat
    def get_to_go(self):
        return self.to_go
    def get_rice(self):
        return self.rice
    def get_beans(self):
        return self.beans
    def get_extra_meat(self):
        return self.extra_meat
    def get_guacamole(self):
        return self.guacamole
    def get_cheese(self):
        return self.cheese
    def get_pico(self):
        return self.pico
    def get_corn(self):
        return self.corn
    def get_cost(self):
        cost = 5.0
        if self.get_meat() in ["chicken", "pork", "tofu"]:
            cost += 1
        elif self.get_meat() == "steak":
            cost += 1.5
        if self.get_extra_meat() and (self.get_meat() != False):
            cost += 1
        if self.get_guacamole():
            cost += 0.75
        return cost


#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())

