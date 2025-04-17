monthly_sales = [42, 38, 33, 38, 40, 45]
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June']

thresold = 35

for sales_amount, month  in zip(monthly_sales, months):
    if sales_amount < thresold:
        print(f"Sales amount {sales_amount} is less than the thresold  in this {month}")
        #break
    else:
        print(f"Sales amount {sales_amount} is greater than the thresold in this {month} ")