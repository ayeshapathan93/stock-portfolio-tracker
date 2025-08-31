def stock_portfolio():
    # Hardcoded stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2800, "MSFT": 310, "AMZN": 135}

    portfolio = {}
    total_value = 0

    print("📊 Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("⚠️ Stock not available!")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty

    print("\n📌 Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_value += value
        print(f"{stock} ({qty} shares) = ${value}")

    print("\n💰 Total Investment Value: $", total_value)

    # Save result in a file
    with open("portfolio.txt", "w") as f:
        f.write("📊 Stock Portfolio Report\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock} ({qty} shares) = ${qty * stock_prices[stock]}\n")
        f.write(f"\n💰 Total Investment Value: ${total_value}\n")

    print("\n✅ Portfolio saved to portfolio.txt")


# Run the stock tracker
stock_portfolio()
