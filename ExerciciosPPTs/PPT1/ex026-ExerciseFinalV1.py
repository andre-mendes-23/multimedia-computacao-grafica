while True:
 try:
    P = float(input("Please enter initial deposit :\n"))
    r = float(input("Please enter yearly interest rate :\n"))
    n = float(input("Please enter number of years :\n"))
 except ValueError:
    print("Sorry, I didn't understand that.")
    break
 else:
    amount = P * (1+r/100)**n
 break
print(f"After {n} years, 100 EUR has grown to {amount:.2f} EUR.")