'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv
with open('chipotle.tsv', mode='rU') as f:
    file_nested_list = []
    for row in csv.reader(f, delimiter='\t'):
        file_nested_list.append(row)

#[your code here]


'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_nested_list[0]
data = file_nested_list[1:]
#[your code here]


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!  Break the problem into steps and then code each step
'''
prices = []
for p in data:
    prices.append(p[4])
prices_clean = []
for x in prices:
    prices_clean.append(x[1:])
prices_squeaky_clean = [float(i) for i in prices_clean]
total = sum(prices_squeaky_clean)
orderid = []
for p in data:
    orderid.append(p[0])
count = len(set(orderid))
total/count
# $18.81
    
#[your code here]


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
drinks = []
for p in data:
    if p[2] =="Canned Soda":
        drinks.append(p[3])
    elif p[2] =="Canned Soft Drink":
        drinks.append(p[3])
item_u = set(drinks)


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
toppings = []
for p in data:
    if "Burrito" in p[2]:
        toppings.append(p[3])
commacount =[]
for p in toppings:
    commacount.append(p.count(',')+1)
total = float(sum(commacount))
count= float(len(toppings))
total/count




#[your code here]


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
Chips = []
for p in data:
    if "Chips" in p[2]:
        Chips.append(p[1:3])
#ok now I have to go to bed.

        

#[your code here]


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''

#[your code here]
