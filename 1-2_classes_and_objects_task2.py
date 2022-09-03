# Declare a class named Goods and add the following attributes (variables) to it:
# title: "Мороженое"
# weight: 154
# tp: "Еда"
# price: 1024
# Then, after declaring the class, change its price attribute to 2048 and add another attribute:
# inflation: 100
# Display the price and the new attribute on the screen


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100

print(Goods.price, Goods.inflation)
