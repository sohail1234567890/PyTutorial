
def find_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

expenses_sergey = [30 ,45, 70 ,90]
expenses_sundar = [40 ,23, 10, 85]

total_expense_sergey = find_total(expenses_sergey)
print("Total sergey's expense :", total_expense_sergey)

total_expense_sundar = find_total(expenses_sundar)
print("Total sunadr's expense:" ,total_expense_sundar)