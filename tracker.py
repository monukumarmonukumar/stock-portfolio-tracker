# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 350,
    "AMZN": 130
}

portfolio = {}
total_value = 0

print("--- Stock Portfolio Tracker ---")
print(f"Available stocks: {', '.join(stock_prices.keys())}")

# Get user input
while True:
    stock_name = input("\nEnter stock symbol (e.g., AAPL) or type 'done' to finish: ").upper()
    
    if stock_name == 'DONE':
        break
    
    if stock_name not in stock_prices:
        print(f"Stock not found. Available stocks are: {list(stock_prices.keys())}")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("Please enter a valid number for quantity.")

# Calculate and display results
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save = input("\nDo you want to save the report to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_report.txt", "w") as f:
        f.write("Stock Portfolio Report\n")
        f.write("----------------------\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        f.write(f"\nTotal Value: ${total_value}\n")
    print("Report saved successfully as 'portfolio_report.txt'")