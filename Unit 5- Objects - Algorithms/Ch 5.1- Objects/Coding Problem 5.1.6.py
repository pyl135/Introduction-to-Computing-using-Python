#Copy both your code and ours from the previous exercise.
#You should copy your Burrito class and our Meat, Rice, and
#Beans classes into this exercise.
#
#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.


#Paste your previous code here.
class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False



#Write your new function here.
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False,
                 corn=False):
        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def get_cost(self):
        money = 5.00
        if self.get_meat() in ["chicken", "pork", "tofu"]:
            money += 1
        if self.get_meat() in ["steak"]:
            money += 1.50
        if self.extra_meat == True and self.get_meat() != False:
            money += 1
        if self.guacamole == True:
            money += 0.75
        return money

    def set_meat(self, meat):
        self.meat.set_value(meat)

    def set_to_go(self, to_go):
        if to_go == True:
            self.to_go = to_go
        else:
            self.to_go = False

    def set_rice(self, rice):
        self.rice.set_value(rice)

    def set_beans(self, beans):
        self.beans.set_value(beans)

    def set_guacamole(self, guacamole):
        guacamole_list = [True, False]
        if guacamole in guacamole_list:
            self.guacamole = guacamole
        else:
            self.guacamole = False

    def set_extra_meat(self, extra_meat):
        if extra_meat in [True, False]:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False

    def set_cheese(self, cheese):
        if cheese in [True, False]:
            self.cheese = cheese
        else:
            self.cheese = False

    def set_pico(self, pico):
        if pico in [True, False]:
            self.pico = pico
        else:
            self.pico = False

    def set_corn(self, corn):
        if corn in [True, False]:
            self.corn = corn
        else:
            self.corn = False

    def get_meat(self):
        return self.meat.get_value()

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice.get_value()

    def get_beans(self):
        return self.beans.get_value()

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
    
    
def total_cost(alist):
    result = 0.0
    for item in alist:
        result += item.get_cost()
    return result


#You can add code below to test your function. We'd suggest
#creating a couple instances of Burrito, adding them to a
#list, then passing that list to total_cost and printing the
#result.

burritoa = Burrito("pork", True, "brown", "pinto")
burritoa.set_meat("chicken")
newBurrito = Burrito( "tofu",False,False,False, extra_meat=True , guacamole=True)
print(newBurrito.get_cost())
print (total_cost([burritoa, newBurrito]))
