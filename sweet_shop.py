


sweets = []
x = 0
while x < 5:
    price_of_sweet = input(("Enter price for the sweet " ).lower() + str(x + 1) + ": ")
    if price_of_sweet[-1].lower() in ("p"):
        new_price_of_sweet = int(price_of_sweet[:-1])
        sweets.append(new_price_of_sweet)
        x += 1
    else:
        print("Enter amount in p")






total_price = sum(sweets)
highest_price = max(sweets)
lowest_price = min(sweets)
average_price = (sum(sweets)/5)
print("total price: {}p".format(total_price) )
print("Average price: {}p ".format(average_price))
print("Highest price: {}p ".format(highest_price))
print("lowest price: {}p ".format(lowest_price))






