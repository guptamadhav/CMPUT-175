import datetime as dt
def product_list():
    products_file = "Assignment 1/transactions_Products.csv"
    with open(products_file, mode = "r") as f:
        p_data = f.readlines()
    products_data = {}
    for i in range(1,len(p_data)):
        data = p_data[i].split(",")
        products_data[data[0]] = data[1], int(data[2][:-1])
    return products_data

def sale_list():
    sales_file = "Assignment 1/transactions_Sales.csv"
    with open(sales_file, mode = "r") as f:
        s_data = f.readlines()
    sales_data = {}
    for i in range(1,len(s_data)):
        data = s_data[i].split(",")
        sales_data[data[0]] = data[1], data[2], int(data[3]), float(data[4][:-1])
    return sales_data

def return_list():
    return_file = "Assignment 1/transactions_Returns.csv"
    with open(return_file, mode = "r") as f:
        r_data = f.readlines()
    return_data = {}
    for i in range(1,len(r_data)):
        data = r_data[i].split(",")
        return_data[data[0]] = data[1][:-1]
    return return_data

def sales_units(products_data, sales_data, return_data):
    units = {}
    discount = {}
    sales = {}
    transactions_per_day = {}
    for i in products_data:
        units[i] = 0
        discount[i] = 0
        sales[i] = 0
    for key, value in sales_data.items():
        if key not in return_data:
            units[value[1]] += value[2]
            discount[value[1]] += (value[2]*value[3])
        if value[0] not in transactions_per_day:
            transactions_per_day[value[0]] = 1
        else:
            transactions_per_day[value[0]] += 1
    for key, value in units.items():
        sales[key] = (products_data[key][1] * value) -(discount[key]*products_data[key][1])
    return units, sales, discount, transactions_per_day

def top_3_sold_units(units_sold, products_data):
    sorted_units_sold = dict(sorted(units_sold.items(), key=lambda item:item[1],reverse=True))
    top_3_sold_units = list(sorted_units_sold.items())[:3]
    for key, value in top_3_sold_units:
        print("{:>20}".format(products_data[key][0])+" "+"{:>3}".format(value))

def top_3_sales_amount(sales_amount, products_data):
    sorted_sales_amount = dict(sorted(sales_amount.items(), key=lambda item: item[1], reverse=True))
    top_3_sales_gen = list(sorted_sales_amount.items())[:3]
    for key, value in top_3_sales_gen:
        print("{:>20}".format(products_data[key][0])+" $"+"{:>10.2f}".format(value))

def turnover(units_sold, sales_amount, discount_amount):
    net_report = {}
    for key, value in units_sold.items():
        name = products_data[key][0]
        total_discounted_amount = discount_amount[key] * products_data[key][1]
        net_report[key] = name, value, sales_amount[key], discount_amount[key]/value*100, total_discounted_amount
    report = dict(sorted(net_report.items(), key=lambda item: item[1][4] ,reverse=True))
    for key, value in report.items():
        print("+---+--------------------+---+-----------+------+-----------+")
        print("|"+"{:>3}".format(key)+"|"+"{:>20}".format(value[0])+"|"+"{:>3}".format(value[1])+"|$"+"{:10,.2f}".format(value[2])+"|"+"{:>5.2f}".format(value[3])+"%|$"+"{:>10.2f}".format(value[4])+"|")
    print("+---+--------------------+---+-----------+------+-----------+")      
def transactions(transactions_per_day): 
    transactions_days = {"Monday" : 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    for key, value in transactions_per_day.items():
        date = dt.datetime(int(key[:4]),int(key[5:7]),int(key[8:10]))
        transactions_days[date.strftime("%A")] = value
    for key, value in transactions_days.items():
        print("{:>19}".format(key)+"{:>3}".format(value))

def return_item(return_data, sales_data, products_data):
    return_items = {}
    for key, value in return_data.items():
        id = sales_data[key][1]
        name = products_data[id][0]
        # amount = sales_data[key][2]
        if id not in return_items:
            return_items[id] = [name, 0]
        return_items[id][1] += 1
    for key,value in return_items.items():
        print("{:>3}".format(key)+" "+"{:>20}".format(value[0])+" "+"{:>3}".format(value[1]))

products_data = product_list()
sales_data = sale_list()
return_data = return_list()
units_sold, sales_amount, discount_amount, transactions_data  = sales_units(products_data, sales_data, return_data)

# Q1) What is the product that led to the larger number of sales in units?
print("1. The product that led to the larger number of sales in units: ")
top_3_sold_units(units_sold, products_data)

# Q2) What is the product that led to the larger number of sales in dollars?
print("\n2. The product that led to the larger number of sales in dollars:")
top_3_sales_amount(sales_amount, products_data)

# Q3) What is the turnover for all sales?
print("\n3. Turnover of Sales:")
turnover(units_sold, sales_amount, discount_amount)

# Q4) What are the number of transactions per weekday?
for key, value in return_data.items():
    transactions_data[value] -= 1
print("\n4. Number of transactions per weekday:")
transactions(transactions_data)

# Q5) What are the returned products?
print("\n5. Returned Items:")
return_item(return_data, sales_data, products_data)

# Q6) What is the performance of each product?
with open("Assignment 1/ transactions_units.txt", mode="w") as f:
    f.write("Product ID, units sold")
    for key, value in units_sold.items():
        f.write(f"\n{key},{value}")