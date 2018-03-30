#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1 to the cost
# - If guacamole is True, add $0.75 to the cost


#Write your code here!
class Burrito:
    def __init__(self,meat,to_go,rice,beans,extra_meat=False, guacamole=False, cheese=False,pico=False,corn=False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
        
    def get_cost(self):
        money = 5.00
        if self.meat in ["chicken", "pork", "tofu"]:
            money += 1
        if self.meat in ["steak"]:
            money += 1.50
        if self.extra_meat == True and self.meat != False: 
            money += 1
        if self.guacamole == True:
            money += 0.75
        return money    
        

    def set_meat(self, meat):
        meat_list = ["chicken", "pork", "steak", "tofu"]
        if meat in meat_list:
            self.meat = meat
        else:
            self.meat = False

    def set_to_go(self, to_go):
        if to_go == True:
            self.to_go = to_go
        else:
            self.to_go = False

    def set_rice(self, rice):
        rice_list = ["brown", "white"]
        if rice in rice_list:
            self.rice = rice
        else:
            self.rice = False

    def set_beans(self, beans):
        beans_list = ["black", "pinto"]
        if beans in beans_list:
            self.beans = beans
        else:
            self.beans = False

    def set_guacamole(self, guacamole):
        guacamole_list = [True, False]
        if guacamole in guacamole_list:
            self.guacamole = guacamole
        else:
            self.guacamole = False

    def set_extra_meat(self,extra_meat):
        if extra_meat in [True,False]:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False

    def set_cheese(self,cheese):
        if cheese in [True,False]:
            self.cheese = cheese
        else:
            self.cheese = False

    def set_pico(self,pico):
        if pico in [True,False]:
            self.pico = pico
        else:
            self.pico = False

    def set_corn(self,corn):
        if corn in [True,False]:
            self.corn = corn
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


#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.
