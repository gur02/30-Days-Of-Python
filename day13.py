def calculate_tax(price):
    tax = price * 0.15
    return tax 
total_tax = calculate_tax(100)
print(f"the calculation tax is: ${total_tax}")