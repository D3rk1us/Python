"""
dictionary = {
    key1: value1,
    key2:value2
}
"""

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}


# Constructor
pizza = dict([('name', 'Pepperoni Pizza'), ('price', 7.9), ('calories_per_slice', 494), ('toppings', ['mozzarella', 'provolone'])])

print(pizza['name'])

# Get value
print(pizza.get('toppings', []))
print(pizza.values())

# Get keys
print(pizza.keys())

# Get items
print(pizza.items())

# Clear items
print(pizza.clear())

# Delete one item
print(pizza.pop('price', 10))

# Update item
pizza.update({'price': 15, 'total_time': 25})
print(pizza.items())

# Loops
products = {
        'Laptop': 990,
        'Smartphone': 600,
        'Tablet': 250,
        'Headphones': 70,
}

for price in products.values():
    print(price)

"""
990
600
250
70
"""

for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)

"""
Laptop
Smartphone
Tablet
Headphones
"""


for product in products.items():
    print(product)

"""
('Laptop', 990)
('Smartphone', 600)
('Tablet', 250)
('Headphones', 70)
"""

for product, price in products.items():
    print(product, price)

"""
Laptop 990
Smartphone 600
Tablet 250
Headphones 70
"""

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

"""
{
    'Laptop': 792, 
    'Smartphone': 480, 
    'Tablet': 200, 
    'Headphones': 56
}
"""

for index, product in enumerate(products.items(), 1):
    print(index, product)

"""
1 ('Laptop', 990)
2 ('Smartphone', 600)
3 ('Tablet', 250)
4 ('Headphones', 70)
"""
