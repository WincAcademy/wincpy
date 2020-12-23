leek_price = 2
print("Leek is" + str(leek_price) + " euro per kilo.")

order = "leek 4"
order_amount = int(order[order.find(" ") :])
sum_total = leek_price * order_amount
print(sum_total)

broccli_price = 2.34
order = "broccoli 1.6"
order_amount = float(order[order.find(" ") :])
sum_total = round(broccli_price * order_amount, 2)
print(str(sum_total) + "kg broccoli costs " + str(sum_total) + "e")
