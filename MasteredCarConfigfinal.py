#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Mastered Car Configurater by Adam Russell
#program structure
#1. set-up car as object - define class & constructor
#2. calculate final price in object
#3. use while/if loops to structure menus
#4. set-up functions to amend properties of object

#program should run as follows
#1. select base car spec - manufacturer & model only
#2. user selects accessories and price is updated
#3. user view/modify order any time

class car:
    def __init__(self, man, mod, p):
        self.manuf = man #car manufacturer - ford, toyota, audi, tesla
        self.model = mod #car model - hatchback, estate, 4x4
        self.engine = "petrol" #car engine - petrol, diseal, hybrid, electric - default option to be changed
        self.colour = "black" #car colour - black, green, red, blue, yellow - default option to be changed
        self.interior = "base" #car interior - base, premium, luxury - default option to be changed
        self.baseprice = p #car price
        self.finalprice = 0.00 #final price with accessories
        
car_models = [["hatchback",10000], ["estate",12000], ["4x4",15000]] 
car_manuf = [["ford",1.1], ["toyota",1.2], ["audi",1.5], ["tesla",1.8]] #car manufacturers price multiplier 
car_engine = [["petrol",1.0],["diseal", 1.1],["hybrid", 1.3],["electric", 1.5]]
car_colour = [["black",0],["green",100],["red",100],["blue",100],["yellow",100]]
car_interior = [["base",1.0],["premium",1.05],["luxury",1.1]]

base_car_spec = []

def base_car():
    print("**********************************************")
    print("Base Car Selection")
    print("please select car manufacturer")
    print("[0] Ford")
    print("[1] Toyota")
    print("[2] Audi")
    print("[3] Tesla")
    
    man_car = -1
    
    while (man_car < 0 or man_car > 3):
        man_car = int(input("make a selection followed by enter"))
    print("**********************************************")
    
    print("**********************************************")
    print("please select car model")
    print("[0] hatchback")
    print("[1] estate")
    print("[2] 4x4")
    mod_car = -1
    
    while (mod_car < 0 or mod_car > 2):
        mod_car = int(input("make a selection followed by enter"))
    print("**********************************************")
    
    base = car(car_manuf[man_car][0], car_models[mod_car][0], car_manuf[man_car][1]*car_models[mod_car][1]) #constructor
    
    base.finalprice = base.baseprice #check for circular referencing
    
    print_car_spec(base)
    
    return base

def print_car_spec(base):
    print("**********************************************")
    print("manufacturer:", base.manuf)
    print("model:", base.model)
    print("engine:", base.engine)
    print("colour:", base.colour)
    print("interior:", base.interior)
    print("base prce:£", base.baseprice)
    print("final price:£", base.finalprice)
    print("**********************************************")
    
def modify_car_spec(base):
    print("**********************************************")
    print("Car Accessories Selection")
    print("please select car engine type")
    print("[0] Petrol")
    print("[1] Diseal")
    print("[2] Hybrid")
    print("[3] Electric")
    eng_car = -1
    
    while (eng_car < 0 or eng_car > 3):
        eng_car = int(input("make a selection followed by enter"))
        
    base.engine = car_engine[eng_car][0]
    print("**********************************************")

    print("**********************************************")
    print("please select car color")
    print("[0] Black")
    print("[1] Green")
    print("[2] Red")
    print("[3] Blue")
    print("[4] Yellow")
    col_car = -1
    
    while (col_car < 0 or col_car > 4):
        col_car = int(input("make a selection followed by enter"))
        
    base.colour = car_colour[col_car][0]
    print("**********************************************")
        
    print("**********************************************")
    print("please select car interior type")
    print("[0] Base")
    print("[1] Premium")
    print("[2] Luxury")
    int_car = -1
    
    while (int_car < 0 or int_car > 2):
        int_car = int(input("make a selection followed by enter"))
        
    base.interior = car_interior[int_car][0]
    print("**********************************************")
    base.finalprice = base.baseprice*car_engine[eng_car][1]*car_interior[int_car][1]+car_colour[col_car][1]
    
    return base
    

# Defining main function
def main():
    print("welcome to Mastered Car Configurater!")
    print("Please first select a base model of car")
    base=base_car()
    
    menu=0
    
    while menu != 4:
        print("please select from the follow options")
        print("**********************************************")
        print("[1] to select base model & manufacturer of car (this resets all option to base)")
        print("[2] to configure model with accessories")
        print("[3] to display full spec & cost")
        print("[4] to close program")
        print("**********************************************")
        menu = input("make a selection followed by enter")
        print(menu)
        
        if int(menu) == 1 :
            print("option [1] selected")
            base=base_car()
        
        elif int(menu) == 2 :
            print("option [2] selected")
            modify_car_spec(base) 
        
        elif int(menu) == 3 :
            print("option [3] selected")
            print_car_spec(base)
            
        elif int(menu) == 4 :
            print("option [4] selected")
            break
                
        else:
            print("incorrect selection")

    print("closing program")
    
    return
    
main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




