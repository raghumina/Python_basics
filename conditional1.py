# 
'''
is_hot = True        # only True conditions gets printed 
cold = False         # false conditions are ignored
if is_hot:
    print("Its a hot day")
    print("drink lots of water")
elif cold:
    print("Take care")
else:
    print("have a good day")
print("enjoy your day")    


# lets write weather system 
# which gives specific messages related to the weather
import random 
list = ["Summer","Winter","Monsoon","Spring"]
mylist = random.choice(list)
if mylist == "Summer":
    print("Its a hot day")
    print("Drink lots of water")
elif mylist == "Winter":
    print("Its a cold day")
    print("Keep yourself warm")
elif mylist == "Monsoon":
    print("Its a rainy day")
    print("Take care")
else:
    print("Its a great day")
    print("enjoy your ")    

'''
# here we will use logical operators

# another program
# lets create a discount calculator 
# if price is greater than 1000 then the customer will get 10% discount
# and if he purchases 5 items also get 10 % discount
# lets start

import random
price = random.randint(800,1400)
items = random.randint(1,10)
if price > 1000 and items >=5:
    discount = .10 * price
    sales_price = price - discount
    print("final price after deductiong discount amount is",discount)
else:
    print("No discount")
