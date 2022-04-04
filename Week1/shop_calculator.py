totaL_price=0

number_of_items=int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid quantity")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    count=i+1
    price=float(input("Price of item {}: ".format(i+1)))
    totaL_price += price

if totaL_price>100:
    discounted_price=totaL_price*0.1

print("Total price for {} items is ${:.2f}".format(count,totaL_price))
