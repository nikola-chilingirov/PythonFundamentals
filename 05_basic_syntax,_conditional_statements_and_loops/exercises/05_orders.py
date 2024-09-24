n = int(input())
price = 0
total_price = 0
for i in range(n):
    ppc = float(input())
    days = int(input())
    cpd = int(input())
    if (ppc < 0.01 or ppc > 100) or (days < 1 or days > 31) or (cpd < 1 or cpd > 2000):
        continue
    else:
        price = ppc * days * cpd
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
