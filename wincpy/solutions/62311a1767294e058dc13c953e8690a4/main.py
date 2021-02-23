leek_price = 2
print("Leek is" + str(leek_price) + " euro per kilo.")

order = "leek 4"
order_amount = int(order[order.find(" ") :])
sum_total = leek_price * order_amount
print(sum_total)

broccoli_price = 2.34
order = "broccoli 1.6"
order_amount = float(order[order.find(" ") :])
sum_total = round(broccoli_price * order_amount, 2)
print(str(order_amount) + "kg broccoli costs " + str(sum_total) + "e")
