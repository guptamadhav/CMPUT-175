# Exercise 1 : Python Warm up
"""
1) Bluebell Greenhouses sells the following Spring flower bulbs. Create a dictionary that stores
this information. Which data should be the keys (must be unique), and which should be the
values? 
--Here flower Bulb Name should be the keys as they are unique for each flower and Price per Bulb 
  should be the value
"""
keys = ["daffodil", "tulip", "crocus", "hyacinth", "bluebell"]
values = [0.35, 0.33, 0.25, 0.75, 0.5]
flower_bulbs_price = {key:value for key, value in zip(keys, values)}
# here zip function returns a tuple by combining two lists

"""
2) Mary has a standing order with Bluebell Greenhouses for 50 daffodil bulbs and 100 tulip
bulbs every year. Create a new dictionary that stores this information. 
"""
order_quantity = {"daffodil": 50, "tulip": 100}

"""
3)Demand for tulips this year has dramatically outpaced demand. As a result, the price of tulip
bulbs has increased by 25%. Update the price of tulip bulbs in the appropriate dictionary.
(Round the price per bulb to 2 decimal places.) 
"""
# as the price of tulip has rise by 25%, multiply its original price by 1.25
tulip_new_price = flower_bulbs_price["tulip"]*1.25
flower_bulbs_price["tulip"] = round(tulip_new_price, 2)

"""
4)This year, Mary would also like to try planting hyacinths. Add 30 hyacinth bulbs to the
dictionary that is storing her order
"""
order_quantity["hyacinth"] = 30

"""
5)Display Mary’s purchase order for this year on the screen. Each line should be formatted as
follows:  where the code for each bulb name is the first three letters of its name, all in capital letters.
The lines should be printed so that the bulb codes are in alphabetical order. 
"""

print("You have purchased the following bulbs: ")
total_amount = 0
total_quant = 0
for i in order_quantity:
    bulb_code = i.upper()[:3]
    price = flower_bulbs_price[i]
    quant = order_quantity[i]
    amount = round(price*quant,2)
    str_amount = str(amount) + "0"
    total_amount += amount
    total_quant += quant
    print("{:5}".format(bulb_code) + " *" + "{:4}".format(quant) + " = $" + "{:6}".format(str_amount))

"""
6)Calculate the total number of bulbs that Mary purchased this year, as well as the total cost of
her order. Include this information at the bottom of her purchase order. Format the total cost
float value so that it is right-aligned in a field width of 6, with 2 decimal places. 
"""
print(f"Thank you for purchasing {total_quant} bulbs from Bluebell Greenhouses. Your total comes to $ {total_amount}.")
